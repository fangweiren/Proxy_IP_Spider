# Redis ���ݿ��ַ
REDIS_HOST = 'localhost'

# Redis �˿�
REDIS_PORT = 6379

# Redis ����
REDIS_PASSWORD = None

REDIS_KEY = 'proxies'

# �����ֵ
MAX_SCORE = 100
MIN_SCORE = 0
INITIAL_SCORE = 10

VALID_STATUS_CODES = [200, 302]

# �������������
POOL_UPPER_THRESHOLD = 10000

# �������
TESTER_CYCLE = 1800
# ��ȡ����
GETTER_CYCLE = 1000

# ����
TESTER_ENABLED = True
GETTER_ENABLED = True
API_ENABLED = True

# ���� API������ץ�ĸ���վ���ĸ�
TEST_URL = 'http://www.baidu.com'

# API ����
API_HOST = '0.0.0.0'
API_PORT = 5555

# �����������
BATCH_TEST_SIZE = 10