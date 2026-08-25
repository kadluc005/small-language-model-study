from src.import_data import names


chars = sorted(list(set(''.join(names))))

itos = {i+1: s for i, s in enumerate(chars)}
itos[0] = '<start>'
itos[27] = '<end>'

stoi = {s:i+1 for i, s in enumerate(chars)}
stoi['<start>'] = 0
stoi['<end>'] = 27