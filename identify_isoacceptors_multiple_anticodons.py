#identifies tRNA isoacceptors based on having multiple unique anticodons for the same amino acid(diffrent anticodon but cding for same aminoacid)
import pandas as pd

# Load data into a DataFrame
file_path = 'filt_seq_info_s.csv'
df = pd.read_csv(file_path)

# Create a dictionary to hold tRNAs grouped by amino acid
tRNA_groups = df.groupby('tRNA_info')['tRNA_info'].apply(list).reset_index(name='tRNAs')

# Split 'tRNA_info' into separate columns for amino acid and anticodon
df[['tRNA', 'Amino_Acid']] = df['tRNA_info'].str.extract(r'(\w+)-(\w+)')
df['Anticodon'] = df['tRNA_info'].str.extract(r'::.*-(\w+)')

# Group by Amino Acid and collect different anticodons
isoacceptors = df.groupby('Amino_Acid')['Anticodon'].unique().reset_index()
isoacceptors = isoacceptors[isoacceptors['Anticodon'].apply(lambda x: len(x) > 1)]

# Extract tRNAs that are isoacceptors
isoacceptor_tRNAs = df[df['Amino_Acid'].isin(isoacceptors['Amino_Acid'])]

# Save the result to a new CSV file
isoacceptor_tRNAs.to_csv('isoacceptors_s.csv', index=False)

print("Isoacceptors have been saved to 'isoacceptors.csv'.")
