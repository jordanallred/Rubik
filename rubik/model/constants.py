from dataclasses import dataclass

'''
Constants used across the microservice 
'''

@dataclass
class Face:
    left = None
    right = None
    letter: str
    
@dataclass
class Panel:
    position: int
    left = None
    right = None
    up = None
    down = None

#-----------------------------------
#  Mapping of cube element positions to mnemonic names
#  Each mnemonic is a three-character pattern, frc, where
#       f indicates the face and is one of F, R, B, L, U, D
#       r indicates the row and is one of T, M, B (for top, middle, bottom, respectively)
#       c indicates the column and is one of L, M, R (for left, middle, right, repectively)
#  The regex for the pattern is r'[FRBLUD][TMB][LMR]'
#
# Front face
FTL = 0
FTM = 1
FTR = 2
FML = 3
FMM = 4
FMR = 5
FBL = 6
FBM = 7
FBR = 8

# Right face
RTL = 9
RTM = 10
RTR = 11
RML = 12
RMM = 13
RMR = 14
RBL = 15
RBM = 16
RBR = 17

# Back face
BTL = 18
BTM = 19
BTR = 20
BML = 21
BMM = 22
BMR = 23
BBL = 24
BBM = 25
BBR = 26

# Left face
LTL = 27
LTM = 28
LTR = 29
LML = 30
LMM = 31
LMR = 32
LBL = 33
LBM = 34
LBR = 35

# Up face
UTL = 36
UTM = 37
UTR = 38
UML = 39
UMM = 40
UMR = 41
UBL = 42
UBM = 43
UBR = 44

#Down face
DTL = 45
DTM = 46
DTR = 47
DML = 48
DMM = 49
DMR = 50
DBL = 51
DBM = 52
DBR = 53

# Cube Params
NUM_ELEMENTS = 54
NUM_FACES = 6
VALID_DIRECTIONS = "FfBbLlRrUu"

# Triggers
FRONT = Face('f')
RIGHT = Face('r')
LEFT = Face('l')
BACK = Face('b')

FRONT.right = RIGHT
FRONT.left = LEFT

RIGHT.right = BACK
RIGHT.left = FRONT

LEFT.right = FRONT
LEFT.left = BACK

BACK.right = LEFT
BACK.left = RIGHT

# Panels
FTL_PANEL = Panel(FTL)
FTM_PANEL = Panel(FTM)
FTR_PANEL = Panel(FTR)
FML_PANEL = Panel(FML)
FMM_PANEL = Panel(FMM)
FMR_PANEL = Panel(FMR)
FBL_PANEL = Panel(FBL)
FBM_PANEL = Panel(FBM)
FBR_PANEL = Panel(FBR)

RTL_PANEL = Panel(RTL)
RTM_PANEL = Panel(RTM)
RTR_PANEL = Panel(RTR)
RML_PANEL = Panel(RML)
RMM_PANEL = Panel(RMM)
RMR_PANEL = Panel(RMR)
RBL_PANEL = Panel(RBL)
RBM_PANEL = Panel(RBM)
RBR_PANEL = Panel(RBR)

BTL_PANEL = Panel(BTL)
BTM_PANEL = Panel(BTM)
BTR_PANEL = Panel(BTR)
BML_PANEL = Panel(BML)
BMM_PANEL = Panel(BMM)
BMR_PANEL = Panel(BMR)
BBL_PANEL = Panel(BBL)
BBM_PANEL = Panel(BBM)
BBR_PANEL = Panel(BBR)

LTL_PANEL = Panel(LTL)
LTM_PANEL = Panel(LTM)
LTR_PANEL = Panel(LTR)
LML_PANEL = Panel(LML)
LMM_PANEL = Panel(LMM)
LMR_PANEL = Panel(LMR)
LBL_PANEL = Panel(LBL)
LBM_PANEL = Panel(LBM)
LBR_PANEL = Panel(LBR)

UTL_PANEL = Panel(UTL)
UTM_PANEL = Panel(UTM)
UTR_PANEL = Panel(UTR)
UML_PANEL = Panel(UML)
UMM_PANEL = Panel(UMM)
UMR_PANEL = Panel(UMR)
UBL_PANEL = Panel(UBL)
UBM_PANEL = Panel(UBM)
UBR_PANEL = Panel(UBR)

DTL_PANEL = Panel(DTL)
DTM_PANEL = Panel(DTM)
DTR_PANEL = Panel(DTR)
DML_PANEL = Panel(DML)
DMM_PANEL = Panel(DMM)
DMR_PANEL = Panel(DMR)
DBL_PANEL = Panel(DBL)
DBM_PANEL = Panel(DBM)
DBR_PANEL = Panel(DBR)

# FRONT
FTL_PANEL.left = LTR_PANEL
FTL_PANEL.up = UBL_PANEL

FTM_PANEL.up = UBM_PANEL

FTR_PANEL.up = UBR_PANEL
FTR_PANEL.right = RTL_PANEL

FML_PANEL.left = LMR_PANEL

FMR_PANEL.right = RML_PANEL

FBL_PANEL.left = LBR_PANEL
FBL_PANEL.down = DTL_PANEL

FBM_PANEL.down = DTM_PANEL

FBR_PANEL.down = DTR_PANEL
FBR_PANEL.right = RBL_PANEL

# RIGHT
RTL_PANEL.left = FTR_PANEL
RTL_PANEL.up = UBR_PANEL

RTM_PANEL.up = UMR_PANEL

RTR_PANEL.up = UTR_PANEL
RTR_PANEL.right = BTL_PANEL

RML_PANEL.left = FMR_PANEL

RMR_PANEL.right = BML_PANEL

RBL_PANEL.left = FBR_PANEL
RBL_PANEL.down = DTR_PANEL

RBM_PANEL.down = DMR_PANEL

RBR_PANEL.down = DBR_PANEL
RBR_PANEL.right = BBL_PANEL

# BACK
BTL_PANEL.left = RTR_PANEL
BTL_PANEL.up = UTR_PANEL

BTM_PANEL.up = UTM_PANEL

BTR_PANEL.up = UTL_PANEL
BTR_PANEL.right = LTL_PANEL

BML_PANEL.left = RMR_PANEL

BMR_PANEL.right = LML_PANEL

BBL_PANEL.left = RBR_PANEL
BBL_PANEL.down = DBR_PANEL

BBM_PANEL.down = DBM_PANEL

BBR_PANEL.down = DBL_PANEL
BBR_PANEL.right = LBL_PANEL

# LEFT
LTL_PANEL.left = BTR_PANEL
LTL_PANEL.up = UTL_PANEL

LTM_PANEL.up = UML_PANEL

LTR_PANEL.up = UBL_PANEL
LTR_PANEL.right = FTL_PANEL

LML_PANEL.left = BMR_PANEL

LMR_PANEL.right = FML_PANEL

LBL_PANEL.left = BBR_PANEL
LBL_PANEL.down = DBL_PANEL

LBM_PANEL.down = DML_PANEL

LBR_PANEL.down = DTL_PANEL
LBR_PANEL.right = FBL_PANEL

# UP
UTL_PANEL.left = LTL_PANEL
UTL_PANEL.up = BTR_PANEL

UTM_PANEL.up = BTM_PANEL

UTR_PANEL.up = BTL_PANEL
UTR_PANEL.right = RTR_PANEL

UML_PANEL.left = LTM_PANEL

UMR_PANEL.right = RTM_PANEL

UBL_PANEL.left = LTR_PANEL
UBL_PANEL.down = FTL_PANEL

UBM_PANEL.down = FTM_PANEL

UBR_PANEL.down = FTR_PANEL
UBR_PANEL.right = RTL_PANEL

# DOWN
DTL_PANEL.left = LBR_PANEL
DTL_PANEL.up = FBL_PANEL

DTM_PANEL.up = FBM_PANEL

DTR_PANEL.up = FBR_PANEL
DTR_PANEL.right = RBL_PANEL

DML_PANEL.left = LBM_PANEL

DMR_PANEL.right = RBM_PANEL

DBL_PANEL.left = LBL_PANEL
DBL_PANEL.down = BBR_PANEL

DBM_PANEL.down = BBM_PANEL

DBR_PANEL.down = BBL_PANEL
DBR_PANEL.right = RBR_PANEL

PANEL_LIST = [FTL_PANEL, FTM_PANEL, FTR_PANEL, FML_PANEL, FMM_PANEL, FMR_PANEL, FBL_PANEL, FBM_PANEL, FBR_PANEL, 
              RTL_PANEL, RTM_PANEL, RTR_PANEL, RML_PANEL, RMM_PANEL, RMR_PANEL, RBL_PANEL, RBM_PANEL, RBR_PANEL,
              BTL_PANEL, BTM_PANEL, BTR_PANEL, BML_PANEL, BMM_PANEL, BMR_PANEL, BBL_PANEL, BBM_PANEL, BBR_PANEL,
              LTL_PANEL, LTM_PANEL, LTR_PANEL, LML_PANEL, LMM_PANEL, LMR_PANEL, LBL_PANEL, LBM_PANEL, LBR_PANEL,
              UTL_PANEL, UTM_PANEL, UTR_PANEL, UML_PANEL, UMM_PANEL, UMR_PANEL, UBL_PANEL, UBM_PANEL, UBR_PANEL,
              DTL_PANEL, DTM_PANEL, DTR_PANEL, DML_PANEL, DMM_PANEL, DMR_PANEL, DBL_PANEL, DBM_PANEL, DBR_PANEL]