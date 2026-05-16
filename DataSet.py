import pandas as pd
import numpy as np

# Set seed for reproducibility
np.random.seed(42)

# Number of students
n = 500

# Generating socio-economic and behavioral variables
student_id = range(1, n + 1)
studytime = np.random.choice([1, 2, 3, 4], size=n, p=[0.2, 0.4, 0.3, 0.1]) # 1: <2 hrs, 4: >10 hrs
medu = np.random.choice([0, 1, 2, 3, 4], size=n, p=[0.05, 0.2, 0.3, 0.25, 0.2]) # Mother's education (0-4)
internet = np.random.choice([0, 1], size=n, p=[0.15, 0.85]) # 1: Yes, 0: No
absences = np.random.poisson(lam=5, size=n) # Average of 5 absences

# Generating Final Grade (G3) on a 0-20 scale with logical correlations
# Base score + studytime boost + internet boost + medu boost - absence penalty + random noise
base_score = 8
noise = np.random.normal(0, 2, n)
G3 = (base_score 
      + (studytime * 1.5) 
      + (internet * 2.0) 
      + (medu * 0.8) 
      - (absences * 0.3) 
      + noise)

# Clip grades to ensure they stay strictly between 0 and 20, and round to integers
G3 = np.clip(np.round(G3), 0, 20).astype(int)

# Create DataFrame
df = pd.DataFrame({
    'student_id': student_id,
    'studytime': studytime,
    'Medu': medu,
    'internet': internet,
    'absences': absences,
    'G3': G3
})

# Save to CSV
file_name = 'cleaned_student_data.csv'
df.to_csv(file_name, index=False)

print(f"Success! Dataset with {n} rows saved as '{file_name}'.")
print("\nFirst 5 rows:")
print(df.head())