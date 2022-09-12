from brownie import FundMe
from scripts.helpful_scripts import get_account


def fund():
    fund_me = FundMe[-1]
    account = get_account()
    entrance_fee = fund_me.getEntranceFee()
    print(entrance_fee)
    fund_me.fund({"from": account, "value": entrance_fee + 1})
    # fund_me.fund({"from": account, "value": entrance_fee + 2 * 10**15})


def withdraw():
    fund_me = FundMe[-1]
    account = get_account()
    fund_me.withdraw({"from": account})


def main():
    # for x in range(0, 3): , Funding multiple times as testing :)
    fund()
    withdraw()
