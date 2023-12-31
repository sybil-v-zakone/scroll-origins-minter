from typing import Tuple

from web3.contract.async_contract import AsyncContract

from config import GAS_DELAY_RANGE, GAS_THRESHOLD
from constants import (
    GET_MINT_PROOF_URL,
    MINTER_CONTRACT_ABI,
    MINTER_CONTRACT_ADDRESS,
    REQUEST_MAX_RETRIES,
)
from core.client import Client
from logger import logger
from utils import gas_delay, retry


class Minter:
    def __init__(self, client: Client) -> None:
        self.client: Client = client
        self.mint_contract: AsyncContract = self.client.w3.eth.contract(
            address=MINTER_CONTRACT_ADDRESS, abi=MINTER_CONTRACT_ABI
        )

    @retry(tries=REQUEST_MAX_RETRIES)
    async def _get_mint_data(self) -> Tuple[str]:
        try:
            data = await self.client.send_get_request(
                url=GET_MINT_PROOF_URL.format(
                    self.client.address, self.client.get_current_timestamp()
                )
            )
            if data is None:
                logger.error(f"Wallet {self.client.address}")
                return None
            return (
                data["metadata"]["firstDeployedContract"],
                data["metadata"]["bestDeployedContract"],
                data["metadata"]["rarityData"],
                data["proof"],
            )
        except Exception as e:
            logger.error(f"Unexpected error while getting mint data: {e}")

    @gas_delay(gas_threshold=GAS_THRESHOLD, gas_delay=GAS_DELAY_RANGE)
    async def mint(self) -> bool:
        mint_data = await self._get_mint_data()
        if mint_data is None:
            return False
        first_deployed_contract, best_deployed_contract, rarity_data, proof = mint_data
        data = self.mint_contract.encodeABI(
            fn_name="mint",
            args=[
                self.client.address,
                [
                    self.client.address,
                    first_deployed_contract,
                    best_deployed_contract,
                    int(rarity_data, 16),
                ],
                proof,
            ],
        )
        tx_hash = await self.client.send_transaction(
            to=self.mint_contract.address, data=data
        )
        if tx_hash is None:
            return False
        return await self.client.verify_tx(tx_hash=tx_hash)
