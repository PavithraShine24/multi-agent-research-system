def human_review(report):
    print("\n" + "="*60)
    print("REPORT FOR REVIEW")
    print("="*60)

    print(report)

    decision = input("\nApprove report? (yes/no): ").lower()

    return decision