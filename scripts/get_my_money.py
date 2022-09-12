from brownie import FundMe, network
from scripts.helpful_scripts import get_account


def take_money():
    if network.show_active() == "rinkeby":
        fund_me = FundMe[-1]
        account = get_account
        print(fund_me.getPrice())
        fund_me.getEntranceFee()
        fund_me.fund({"from": account, "value": 3 * 10**16})
        fund_me.withdraw({"from": account})


def main():
    take_money()


# This file is just for trying random stuff
