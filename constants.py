from utils import read_from_json

# file configuration
PRIVATE_KEYS_FILE_PATH = "data/private_keys.txt"
PROXIES_FILE_PATH = "data/proxies.txt"
DATABASE_FILE_PATH = "data/database.json"

# CLIENT CONFIGURATION
VERIFY_TX_TIMEOUT = 300
REQUEST_MAX_RETRIES = 10
WAIT_FOR_DEPOSIT_DELAY_RANGE = [60, 60]


# regex for matching the valid proxy format
PROXY_PATTERN = r"^([^:@\s]+):([^:@\s]+)@([a-zA-Z0-9.-]+|\d+\.\d+\.\d+\.\d+):(\d+)$"

# logs
LOGS_FILE_PATH = "data/logs/logs.log"

# OKX
OKX_WITHDRAW_TRIES = 5
OKX_WITHDRAW_DELAY_RANGE = [60, 60]
OKX_WAIT_FOR_WITHDRAWAL_FINAL_STATUS_DELAY_RANGE = [10, 10]
OKX_WAIT_FOR_WITHDRAWAL_FINAL_STATUS_ATTEMPTS = 100

# ORBITER
ORBITER_ARB_SCROLL_TRADING_FEE = 0.0012
ORBITER_MIN_SENT_VALUE = 0.001
ARBITRUM_ORBITER_CONTRACT_ADDRESS = "0x80C67432656d59144cEFf962E8fAF8926599bCF8"

# MINTER
MINTER_CONTRACT_ADDRESS = "0x74670A3998d9d6622E32D0847fF5977c37E0eC91"
MINTER_CONTRACT_ABI = read_from_json(file_path="core/abi/Minter_ABI.json")

GET_MINT_PROOF_URL = "https://nft.scroll.io/p/{}.json?timestamp={}"
