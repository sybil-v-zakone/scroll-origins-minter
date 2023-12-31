from dataclasses import dataclass

from config import ARBITRUM_RPC_ENDPOINT, MAINNET_RPC_ENDPOINT, SCROLL_RPC_ENDPOINT


@dataclass
class Chain:
    name: str
    chain_id: int
    coin_symbol: str
    rpc: str
    explorer: str | None = None
    okx_chain_name: str | None = None
    okx_withdrawal_fee: str | None = None
    orbiter_id: str | None = None


SCROLL = Chain(
    name="SCROLL",
    chain_id=534352,
    coin_symbol="ETH",
    explorer="https://scrollscan.com/",
    rpc=SCROLL_RPC_ENDPOINT,
    orbiter_id="9019",
)

ARBITRUM = Chain(
    name="ARBITRUM",
    chain_id=42161,
    coin_symbol="ETH",
    explorer="https://arbiscan.io/",
    rpc=ARBITRUM_RPC_ENDPOINT,
    okx_chain_name="Arbitrum One",
    okx_withdrawal_fee=0.0001,
)

MAINNET = Chain(
    name="Ethereum Mainnet", chain_id=1, coin_symbol="ETH", rpc=MAINNET_RPC_ENDPOINT
)
