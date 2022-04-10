def Test(values):
    for value in values:
        print(value)
    print(f"{len(values)} values have been tested")


def main():
    print("In main function")
    Test([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])


if __name__ == '__main__':
    main()