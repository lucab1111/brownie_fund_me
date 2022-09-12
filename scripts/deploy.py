from brownie import FundMe, MockV3Aggregator, config, network
from scripts.helpful_scripts import (
    deploy_mocks,
    get_account,
    LOCAL_BLOCKCHAIN_ENVIRONMENTS,
)


def deploy_fund_me():
    account = get_account()
    if network.show_active() not in LOCAL_BLOCKCHAIN_ENVIRONMENTS:
        price_feed_address = config["networks"][network.show_active()][
            "eth_usd_price_feed"
        ]
    else:
        mock_aggregator = deploy_mocks()
        price_feed_address = MockV3Aggregator[-1]
    fund_me = FundMe.deploy(
        price_feed_address,
        {"from": account},
        publish_source=config["networks"][network.show_active()].get("verify"),
    )
    # .get("verify") used instead of ["verify"] so that if verify isnt specified in config, False is returned instead of an index error
    return fund_me


def main():
    deploy_fund_me()
