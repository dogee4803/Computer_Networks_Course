import pandas as pd
import random
from datetime import datetime

def generate_data(file_path):
    # Create sample data
    data = {
        'Timestamp': [],
        'Wheel Rotation Count': []
    }
    
    start_time = datetime(2023, 10, 13, 8, 0)
    
    for i in range(20):
        timestamp = start_time + pd.DateOffset(minutes=i)
        data['Timestamp'].append(timestamp.strftime('%d.%m.%y %H:%M'))
        
        if i == 0:
            data['Wheel Rotation Count'].append(100)
        else:
            data['Wheel Rotation Count'].append(data['Wheel Rotation Count'][i-1] + random.randint(1, 5))

    df = pd.DataFrame(data)

    df.to_excel(file_path, index=False)