# Misc options.
VERBOSITY = 1

# Neural network options.
INPUT_DIM = (3, 64, 64)
SERIAL_INPUT_DIM = (3, 32, 32)

OUTPUT_DIM = 39
SERIAL_OUTPUT_DIM = 36

MAX_GPU_FRACTION = 0.4

CONV_FILTERS = 32

CONV_LAYERS = 4

KERNEL_SIZE = 5

USE_BIAS = False

REGULARIZER_CONST = 0.001

LEARNING_RATE = 0.02

MOMENTUM = 0.9

WEIGHT_DECAY = 1e-4

MODULE_BATCH_SIZE = 128
SERIAL_BATCH_SIZE = 128

EPOCHS_PER_BATCH = 5
SERIAL_EPOCHS_PER_BATCH = 10

VALIDATION_SPLIT = 0.3

LABELS = [
    "Nothing (Side)",
    "Big battery",
    "Small batteries",
    "Serial number",
    "Metal piece without parallel port",
    "Parallel port",
    "Lit SIG indicator",
    "Unlit SIG indicator",
    "Lit NSA indicator",
    "Unlit NSA indicator",
    "Lit BOB indicator",
    "Unlit BOB indicator",
    "Lit FRQ indicator",
    "Lit SND indicator",
    "Unlit SND indicator",
    "Lit CLR indicator",
    "Unlit CLR indicator",
    "Lit CAR indicator",
    "Unlit CAR indicator",
    "Lit IND indicator",
    "Lit MSA indicator",
    "Unlit MSA indicator",
    "Lit TRN indicator",
    "Unlit TRN indicator",
    "Lit FRK indicator",
    "Unlit FRK indicator",
    "Nothing (Front)",
    "Timer",
    "Wires",
    "Button",
    "Symbols",
    "Simon Says",
    "Wire Sequence",
    "Complicated Wires",
    "Memory Game",
    "Who's On First?",
    "Maze",
    "Password",
    "Morse"
]

# Image analysis specific
SERIAL_MIN_RED = (110, 0, 0)
SERIAL_MAX_RED = (255, 99, 71)

WIRE_COLOR_RANGE = [
    ((0, 0, 0), (20, 20, 20)),
    ((220, 220, 0), (255, 255, 20)),
    ((30, 30, 180), (100, 100, 255)),
    ((210, 210, 210), (255, 255, 255)),
    ((139, 0, 0), (255, 99, 71))
]
