import argparse

# Simulated price data
def get_prices(product_name):
    prices = {
        "Amazon": "₹1,999",
        "Flipkart": "₹1,899",
        "Croma": "₹2,049"
    }
    return prices

def main():
    parser = argparse.ArgumentParser(
        description="Compare product prices across e-commerce platforms."
    )
    parser.add_argument(
        "product",
        type=str,
        help="Name of the product to compare"
    )

    args = parser.parse_args()
    product = args.product

    print(f"\n🔍 Searching prices for: {product}\n")
    prices = get_prices(product)

    for site, price in prices.items():
        print(f"{site}: {price}")

if __name__ == "__main__":
    main()


