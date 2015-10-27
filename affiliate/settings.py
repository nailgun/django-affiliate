# -*- coding: utf-8 -*-
from django.conf import settings
from decimal import Decimal as D


ALLOW_MISSING_SESSION = getattr(settings, 'AFFILIATE_ALLOW_MISSING_SESSION', False)
BANNER_FOLDER = getattr(settings, 'AFFILIATE_BANNER_PATH', 'affiliate')
AFFILIATE_MODEL = getattr(settings, 'AFFILIATE_AFFILIATE_MODEL', 'affiliate.Affiliate')
PARAM_NAME = getattr(settings, 'AFFILIATE_PARAM_NAME', 'aid')
REWARD_AMOUNT = getattr(settings, 'AFFILIATE_REWARD_AMOUNT', 10)
REWARD_PERCENTAGE = getattr(settings, 'AFFILIATE_REWARD_PERCENTAGE', True)
SAVE_IN_SESSION = getattr(settings, 'AFFILIATE_SAVE_IN_SESSION', True)
SESSION_AGE = getattr(settings, 'AFFILIATE_SESSION_AGE', 5 * 24 * 60 * 60)
DEFAULT_LINK = getattr(settings, 'AFFILIATE_DEFAULT_LINK', '/')
# deprecated
START_AID = getattr(settings, 'AFFILIATE_START_AID', "1000")
DEFAULT_CURRENCY = getattr(settings, 'AFFILIATE_DEFAULT_CURRENCY', "USD")
MIN_REQUEST_AMOUNT = getattr(settings, 'AFFILIATE_MIN_BALANCE_FOR_REQUEST', D('1.0'))