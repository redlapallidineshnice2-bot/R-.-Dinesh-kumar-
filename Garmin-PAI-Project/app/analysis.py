import sqlite3
import pandas as pd
import matplotlib.pyplot as plt

def run_analysis():
    # Connect to database
    conn = sqlite3.connect('data/physical_activity.db')
    df = pd.read_sql_query("SELECT * FROM daily_activities", conn)
    
    if df.empty:
        print("Database is empty!")
        return

    # 1. Calculate Average PAI per Subject (Replicating the research logic)
    avg_pai = df.groupby('subject_id')['pai_score'].mean()
    
    print("--- Results ---")
    print(avg_pai)

    # 2. Correlation (Replicating Table II)
    correlation = df['steps'].corr(df['active_mins'])
    print(f"\nCorrelation (Steps vs Active Mins): {correlation:.4f}")

    # 3. IMPROVED PLOT: Show Subject Names instead of 0, 1, 2
    plt.figure(figsize=(10, 6))
    avg_pai.plot(kind='bar', color='skyblue')
    plt.title("Physical Activity Index (PAI) per Subject (Replicating Fig 3)")
    plt.xlabel("Subject ID")
    plt.ylabel("Average PAI %")
    plt.xticks(rotation=0)
    plt.grid(axis='y', linestyle='--', alpha=0.7)
    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    run_analysis()