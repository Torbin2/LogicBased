from enum import IntEnum

class TileTypes(IntEnum):
    WIRE_G = 1
    WIRE_B = 2

    AND_GATE = 3
    OR_GATE = 4
    XOR_GATE = 5
    NOT_GATE = 6
    TRANSISTOR = 7

    BUTTON = 8
    BRIDGE = 9

    AAA = 0

    # WIRES = [WIRE_B, WIRE_G]
    # LOGIC_GATES = [AND_GATE, OR_GATE, XOR_GATE, NOT_GATE, TRANSISTOR]
    
    #not usable
    SHIFT_TILE = 11