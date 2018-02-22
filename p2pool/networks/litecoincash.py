from p2pool.bitcoin import networks

PARENT = networks.nets['litecoincash']

P2P_PORT = 62468
WORKER_PORT = 5555

SHARE_PERIOD = 20 # seconds
CHAIN_LENGTH = 24*60*60//10 # shares
REAL_CHAIN_LENGTH = 24*60*60//10 # shares
TARGET_LOOKBEHIND = 150 # shares
SPREAD = 12 # blocks
MIN_TARGET = 0
MAX_TARGET = 2**256//2**20 - 1

VERSION_CHECK = lambda v: None if 150001 <= v else 'Litecoin Cash version too old. Upgrade to 0.15.0.1 or newer!'
VERSION_WARNING = lambda v: None
SOFTFORKS_REQUIRED = set(['bip65', 'csv', 'segwit'])
MINIMUM_PROTOCOL_VERSION = 3301
NEW_MINIMUM_PROTOCOL_VERSION = 3301
SEGWIT_ACTIVATION_VERSION = 33
BLOCK_MAX_SIZE = 1000000
BLOCK_MAX_WEIGHT = 4000000

BOOTSTRAP_ADDRS = 'p2p-a.minelcc.net p2p-b.minelcc.net p2p-c.minelcc.net'.split(' ')
ANNOUNCE_CHANNEL = '#p2pool-lcc'

IDENTIFIER = '110a463717b751fd'.decode('hex')
PREFIX = 'dd5c11effc962530'.decode('hex')

PERSIST = True # SET THIS TO FALSE UNTIL THE SHARE CHAIN IS BOOTSTRAPPED
