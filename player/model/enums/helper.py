def from_str(label, enum_type):
    return enum_type[label.upper().replace(' ', '_')]
