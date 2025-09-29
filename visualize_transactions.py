import matplotlib.pyplot as plt
import random


def generate_transactions(n):
    """Generate a list of random transaction amounts"""
    return [random.randint(1, 100) for _ in range(n)]


def plot_transactions(transactions):
    """Plot a bar chart of transaction amounts"""
    plt.figure(figsize=(10, 6))
    plt.bar(range(len(transactions)), transactions)
    plt.title('Sample Blockchain Transaction Amounts')
    plt.xlabel('Transaction')
    plt.ylabel('Amount')
    plt.tight_layout()
    plt.savefig('transactions.png')
    plt.show()


def main():
    data = generate_transactions(20)
    plot_transactions(data)


if __name__ == '__main__':
    main()
