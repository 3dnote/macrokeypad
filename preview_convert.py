import json

HID_MAP = {
    'A': 0x04, 'B': 0x05, 'C': 0x06, 'D': 0x07, 'E': 0x08,
    'F1': 0x3A,
    'Enter': 0x28, 'Esc': 0x29, 'Tab': 0x2B, 'Space': 0x2C,
    'PgUp': 0x4B, 'PgDn': 0x4E, 'Home': 0x4A, 'End': 0x4D,
    'Left': 0x50, 'Right': 0x4F, 'Up': 0x52, 'Down': 0x51
}

REVERSE_HID = {v: k for k, v in HID_MAP.items()}

with open('web/sample_payload.json','r',encoding='utf-8') as f:
    data = json.load(f)

out_layers = []
for l_idx, layer in enumerate(data.get('layers', [])):
    keys = []
    for k_idx, k in enumerate(layer.get('keys', [])):
        entry = {'type': k.get('type',1), 'key':'', 'macro':''}
        if entry['type'] == 3:
            entry['macro'] = k.get('macro','')
        else:
            k1 = int(k.get('key1',0) or 0)
            if k1 in REVERSE_HID:
                entry['key'] = REVERSE_HID[k1]
            elif k1 > 0:
                entry['key'] = str(k1)
            else:
                entry['key'] = ''
        keys.append(entry)
    # pad to 11
    while len(keys) < 11:
        keys.append({'type':1,'key':'','macro':''})
    out_layers.append(keys)

# Print compact preview: first layer first 9 keys as labels/macros
print('Preview: Layer 0 (first 9 keys)')
for i in range(9):
    e = out_layers[0][i]
    if e['type'] == 3:
        print(f'K{i+1}: macro="{e["macro"]}"')
    else:
        print(f'K{i+1}: key="{e["key"]}"')

print('\nFull converted state.layers JSON:')
print(json.dumps(out_layers, ensure_ascii=False, indent=2))
