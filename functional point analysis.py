def get_fp_weight(component, complexity):
    weights = {
        "EI": {"low": 3, "average": 4, "high": 6},
        "EO": {"low": 4, "average": 5, "high": 7},
        "EQ": {"low": 3, "average": 4, "high": 6},
        "ILF": {"low": 7, "average": 10, "high": 15},
        "EIF": {"low": 5, "average": 7, "high": 10},
    }
    return weights[component][complexity]


def calculate_ufp():
    components = ["EI", "EO", "EQ", "ILF", "EIF"]
    ufp = 0

    for comp in components:
        count = int(input(f"Enter number of {comp}: "))
        complexity = input(f"Enter complexity of {comp} (low/average/high): ").lower()
        weight = get_fp_weight(comp, complexity)
        ufp += count * weight

    return ufp


def calculate_vaf():
    print("\nEnter values for 14 General System Characteristics (0 to 5):")
    total_gsc = 0
    for i in range(1, 15):
        value = int(input(f"GSC {i}: "))
        total_gsc += value

    vaf = 0.65 + (0.01 * total_gsc)
    return vaf


def main():
    print("=== Function Point Analysis Calculator ===\n")

    ufp = calculate_ufp()
    print(f"\nUnadjusted Function Points (UFP): {ufp}")

    vaf = calculate_vaf()
    print(f"Value Adjustment Factor (VAF): {vaf:.2f}")

    afp = ufp * vaf
    print(f"\nAdjusted Function Points (AFP): {afp:.2f}")


if __name__ == "__main__":
    main()
