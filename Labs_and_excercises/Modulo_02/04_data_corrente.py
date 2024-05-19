from datetime import datetime

questo_momento = datetime.now()
data_corrente = questo_momento.date()
ora_corrente = questo_momento.strftime('%H:%M:%S')

print(f"La data corrente è: {data_corrente}")
print(f"L'ora corrente è: {ora_corrente}")
