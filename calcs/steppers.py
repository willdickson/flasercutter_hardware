step_per_rev = 200
ustep_per_step = 4
rev_per_mm = 0.025*25.4
gear_ratio = 3

ustep_per_mm = step_per_rev*ustep_per_step*(1.0/rev_per_mm)*gear_ratio

print(f'ustep_per_mm: {ustep_per_mm}')
