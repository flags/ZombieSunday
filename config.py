# Author list:
#     Luke Martin <ltmartin@bsu.edu>
#     Michael Milkovic <mlmilkovic@bsu.edu>
#     Derek Onay <dsonay@bsu.edu>
#     Ryan Wiesjahn <rwiesjahn@bsu.edu>

# NOTES:
# TIME, RATE, DURATION, etc. are all in seconds.
# The formulas the modifiers are used in are shown behind the modifier so you can tell how it is used.
# For weapons: ADD_PLAYER_SPEED is if the players speed should be added to the bullet speed.
# For weapons with _FORCE_HSPEED: The zombie's hspeed is set to: bullet's HSPEED + _FORCE_HSPEED
#     Except for LOBFORCE: The zombie's hspeed is set to: _FORCE_HSPEED

# GAME CONFIG
TITLE = 'Zombie Sunday'
WINDOW_SIZE = (1280, 720)
FPS = 60
RES_DIR = 'res'
FONT_PROGGY = 'res/fonts/ProggySquare.ttf'
FONT_LOMBRIZ = 'res/fonts/lombriz.tff'
HIGHSCORES = []

# SOUNDS
SOUND_MUSIC = 'sounds/squired.xm'
SOUND_BUTTON = 'sounds/button_chime.wav'
SOUND_DOOR = 'sounds/door_open.wav'
SOUND_GUN_GENERIC = 'sounds/gun_generic.wav'
SOUND_GUN_BEAM = 'sounds/gun_beam.wav'
SOUND_ZOMBIE_GROAN = 'sounds/zombie_groan.wav'
SOUND_ZOMBIE_GROAN_2 = 'sounds/zombie_groan_2.wav'
SOUND_ZOMBIE_YELL = 'sounds/zombie_yell.wav'

# UI POSITIONS
LOGO_POS = ((WINDOW_SIZE[0] / 2) - 338, 30)
BUTTON_START_POS = ((WINDOW_SIZE[0] / 2) - 165, 200)
BUTTON_HOWTO_POS = ((WINDOW_SIZE[0] / 2) - 110, 320)
BUTTON_QUIT_POS = ((WINDOW_SIZE[0] / 2) - 150, 440)

BOX_BG_POS = (417, 177)
BOX_2_BG_POS = (417, 144)
BUTTON_NEXT_LEVEL_POS = (BOX_BG_POS[0] + 117, BOX_BG_POS[1] + 230)
BUTTON_EXIT_TO_TITLE_POS = (BOX_2_BG_POS[0] + 44, BOX_2_BG_POS[1] + 370)
LVL_COMPLETE_TITLE_POS = (BOX_BG_POS[0] + 94, BOX_BG_POS[1] + 22)
LVL_COMPLETE_GAME_SCORE_POS = (BOX_BG_POS[0] + 130, BOX_BG_POS[1] + 80)
LVL_COMPLETE_TIME_SCORE_POS = (BOX_BG_POS[0] + 130, BOX_BG_POS[1] + 130)
LVL_COMPLETE_TOTAL_SCORE_POS = (BOX_BG_POS[0] + 130, BOX_BG_POS[1] + 180)
LVL_COMPLETE_KILLS_POS = (BOX_BG_POS[0] + 130, BOX_BG_POS[1] + 124)
LVL_FAIL_OUT_OF_TIME_POS = (BOX_2_BG_POS[0] + 36, BOX_2_BG_POS[1] + 20)
LVL_FAIL_YOU_DIED_POS = (BOX_2_BG_POS[0] + 55, BOX_2_BG_POS[1] + 20)
LVL_FAIL_TITLE_POS = (BOX_2_BG_POS[0] + 132, BOX_2_BG_POS[1] + 130)
LVL_FAIL_SCORES_POS = (BOX_2_BG_POS[0]  + 20, BOX_2_BG_POS[1] + 185)
LVL_FAIL_KILLS_POS = (BOX_2_BG_POS[0]  + 190, BOX_2_BG_POS[1] + 185)
LVL_FAIL_DATE_POS = (BOX_2_BG_POS[0]  + 300, BOX_2_BG_POS[1] + 185)

WEAPON_BG_POS = (20, 20)
WEAPON_STR_POS = (20, 95)
HEALTH_BG_POS = (150, 20)
HEALTH_BAR_POS = (152,22)
HEALTH_STR_POS = (374, 22)
SUPPLY_BG_POS = (150, 56)
SUPPLY_BAR_POS = (152,58)
SUPPLY_STR_POS = (374, 58)
CLOCK_STR_POS = (WINDOW_SIZE[0] / 2, 20)
TOTAL_SUPPLY_BG_POS = (WINDOW_SIZE[0] - 234, 20)
TOTAL_SUPPLY_BAR_POS = (WINDOW_SIZE[0] - 232, 22)
TOTAL_SUPPLY_STR_POS = (WINDOW_SIZE[0] - 330, 22)
LEVEL_STR_POS = (WINDOW_SIZE[0] - 232, 58)
SCORE_STR_POS = (WINDOW_SIZE[0] - 232, 88)
KILLS_STR_POS = (WINDOW_SIZE[0] - 232, 118)

ATTACHMENT_1_POS = (WEAPON_BG_POS[0] + 12, WEAPON_BG_POS[1] + 12)
ATTACHMENT_2_POS = (WEAPON_BG_POS[0] + 12 + 65, WEAPON_BG_POS[1] + 12)

# LEVEL POSITIONS
SUN_POS = (WINDOW_SIZE[0] - 250, 20)
BACKGROUND_1_POS = (0, WINDOW_SIZE[1] - 245)
BACKGROUND_2_POS = (0, WINDOW_SIZE[1] - 192)
CLOUD_1_POS = (WINDOW_SIZE[0] - 100, 10)
CLOUD_2_POS = (WINDOW_SIZE[0] / 2, 200)
CLOUD_3_POS = (0, 100)
GROUND_POS = (0, WINDOW_SIZE[1] - 96)
GROUND_TOP_POS = (0, GROUND_POS[1] - 10)

PLAYER_POS = (10, GROUND_POS[1] - 155)
HOME_POS = (5, GROUND_POS[1] - 430)
BUILDING_POS = (0, GROUND_POS[1] - 430)
DOOR_POS = (260, GROUND_POS[1] - 206) # xPos is relative to BUILDING
ZOMBIE_POS = (0, GROUND_POS[1] - 155)
ATTACHMENT_POS = (0, GROUND_POS[1] - 55)

# LEVEL CONFIG
LEVEL_SIZE = 10
GROUND_WIDTH = 1600
GROUND_HEIGHT = 96
TITLE_SCROLL_SPEED = 100

LEVEL_TIME = 120
BUILDING_RANGE = [15, 25, 100] # [min, max, multiplier]. randint(min, max) * multiplier
SUPPLY_RANGE = [5,8] # [min, max].  Random amount of supplies (between min and max) you get from scavaging buildings / picking up.
SUPPLY_GOAL = 40
SCAVANGE_DURATION = 4 # Amount of time you are in a building scavaging
SCAVANGE_SCORE = 100
TIME_SCORE = 3 # Score to add per second left when you complete a stage
ZOMBIE_MAX = 5
ZOMBIE_SPAWN_RATE = 4

ZOMBIE_MAX_MOD = 1 # ZOMBIE_MAX += ZOMBIE_MAX_MOD * level.stage
ZOMBIE_SPAWN_RATE_MOD = .98 # ZOMBIE_SPAWN_TIME *= pow(ZOMBIE_SPAWN_TIME_MOD, level.stage)
ZOMBIE_HSPEED_MOD = 10 # ZOMBIE_HSPEED += ZOMBIE_HSPEED_MOD * level.stage
ZOMBIE_DAMAGE_MOD = 5 # ZOMBIE_DAMAGE += ZOMBIE_DAMAGE_MOD * level.stage
ZOMBIE_HEALTH_MOD = 10 # ZOMBIE_HEALTH += ZOMBIE_HEALTH_MOD * level.stage
ZOMBIE_ATTACK_RATE_MOD = .98 # ZOMBIE_ATTACK_RATE *= pow(ZOMBIE_ATTACK_RATE_MOD, level.stage)
ZOMBIE_SCORE_MOD = 10 # ZOMBIE_SCORE += ZOMBIE_SCORE_MOD * level.stage
BUILDING_DISTANCE_MOD = 20 # BUILDING_RANGE += BUILDING_DISTANCE_MOD * level.stage
SUPPLY_GOAL_MOD = 10 # SUPPLY_GOAL += SUPPLY_GOAL_MOD * level.stage
SCAVANGE_SCORE_MOD = 10 # SCAVANGE_SCORE += SCAVANGE_SCORE_MOD * level.stage
TIME_SCORE_MOD = 1 # TIME_SCORE += TIME_SCORE_MOD * level.stage

# ENTITY CONFIG
ENTITY_GRAVITY = 20
ENTITY_VSPEED = 200
ENTITY_HSPEED = 200
ENTITY_HEALTH = 500

PLAYER_HEALTH = 100
PLAYER_HSPEED = 400
PLAYER_AMMO = 60
PLAYER_SUPPLY_MAX = 15

ZOMBIE_HEALTH = 75
ZOMBIE_HSPEED = 75
ZOMBIE_DAMAGE = 6
ZOMBIE_ATTACK_RATE = 1
ZOMBIE_SCORE = 100

# WEAPON CONFIG
DEFAULT_RATE = .7
DEFAULT_AMMO_CONSUMPTION = 1
DEFAULT_DURATION = 1
DEFAULT_HSPEED = 600
DEFAULT_DAMAGE = 15
DEFAULT_ADD_PLAYER_SPEED = True

SPEED_RATE = .5
SPEED_AMMO_CONSUMPTION = 1
SPEED_DURATION = 1
SPEED_HSPEED = 1000
SPEED_DAMAGE = 10
SPEED_ADD_PLAYER_SPEED = True

SPEEDSPEED_RATE = .1
SPEEDSPEED_AMMO_CONSUMPTION = 1
SPEEDSPEED_DURATION = 1
SPEEDSPEED_HSPEED = 1800
SPEEDSPEED_DAMAGE = 8
SPEEDSPEED_ADD_PLAYER_SPEED = True

SPEEDFIRE_RATE = 1
SPEEDFIRE_AMMO_CONSUMPTION = 1
SPEEDFIRE_DURATION = 1
SPEEDFIRE_HSPEED = 700
SPEEDFIRE_DAMAGE = 6
SPEEDFIRE_ADD_PLAYER_SPEED = True
SPEEDFIRE_FIRE_DAMAGE = 10
SPEEDFIRE_FIRE_DURATION = 3
SPEEDFIRE_FIRE_RATE = .5

SPEEDLOB_RATE = 1
SPEEDLOB_AMMO_CONSUMPTION = 1
SPEEDLOB_DURATION = 5
SPEEDLOB_HSPEED = 700
SPEEDLOB_VSPEED = -400
SPEEDLOB_GRAVITY = 50
SPEEDLOB_ADD_PLAYER_SPEED = True
SPEEDLOB_EXPLOSION_DURATION = 1
SPEEDLOB_EXPLOSION_DAMAGE = 5

SPEEDFORCE_RATE = 1
SPEEDFORCE_AMMO_CONSUMPTION = 1
SPEEDFORCE_DURATION = .7
SPEEDFORCE_HSPEED = 1000
SPEEDFORCE_DAMAGE = 0
SPEEDFORCE_ADD_PLAYER_SPEED = True
SPEEDFORCE_FORCE_HSPEED = 100
SPEEDFORCE_FORCE_VSPEED = -220

FIRE_RATE = 1
FIRE_AMMO_CONSUMPTION = 1
FIRE_DURATION = .7
FIRE_HSPEED = 300
FIRE_DAMAGE = 10
FIRE_ADD_PLAYER_SPEED = True
FIRE_FIRE_DAMAGE = 10
FIRE_FIRE_DURATION = 3
FIRE_FIRE_RATE = .5

FIREFIRE_RATE = .3 # Determines how often ammo is consumed (since it is a flamethower)
FIREFIRE_AMMO_CONSUMPTION = 1
FIREFIRE_DAMAGE = 1
FIREFIRE_FIRE_DAMAGE = 10
FIREFIRE_FIRE_DURATION = 3
FIREFIRE_FIRE_RATE = .5

FIRELOB_RATE = 1
FIRELOB_AMMO_CONSUMPTION = 1
FIRELOB_DURATION = 5
FIRELOB_HSPEED = 500
FIRELOB_VSPEED = -500
FIRELOB_GRAVITY = 20
FIRELOB_ADD_PLAYER_SPEED = True
FIRELOB_EXPLOSION_DURATION = 1
FIRELOB_EXPLOSION_DAMAGE = 5
FIRELOB_FIRE_DAMAGE = 10
FIRELOB_FIRE_DURATION = 3
FIRELOB_FIRE_RATE = .5

FIREFORCE_RATE = 1
FIREFORCE_AMMO_CONSUMPTION = 1
FIREFORCE_DURATION = .7
FIREFORCE_HSPEED = 500
FIREFORCE_DAMAGE = 0
FIREFORCE_ADD_PLAYER_SPEED = True
FIREFORCE_FORCE_HSPEED = 100
FIREFORCE_FORCE_VSPEED = -220
FIREFORCE_FIRE_DAMAGE = 10
FIREFORCE_FIRE_DURATION = 3
FIREFORCE_FIRE_RATE = .5

LOB_RATE = 1
LOB_AMMO_CONSUMPTION = 1
LOB_DURATION = 5
LOB_HSPEED = 500
LOB_VSPEED = -500
LOB_GRAVITY = 20
LOB_ADD_PLAYER_SPEED = True
LOB_EXPLOSION_DURATION = 1
LOB_EXPLOSION_DAMAGE = 5

LOBLOB_RATE = 1
LOBLOB_AMMO_CONSUMPTION = 1
LOBLOB_DURATION = 5
LOBLOB_HSPEED = 500
LOBLOB_VSPEED = -500
LOBLOB_GRAVITY = 20
LOBLOB_ADD_PLAYER_SPEED = True
LOBLOB_EXPLOSION_DURATION = 1
LOBLOB_EXPLOSION_DAMAGE = 5

LOBFORCE_RATE = 1
LOBFORCE_AMMO_CONSUMPTION = 1
LOBFORCE_DURATION = 5
LOBFORCE_HSPEED = 500
LOBFORCE_VSPEED = -500
LOBFORCE_GRAVITY = 20
LOBFORCE_ADD_PLAYER_SPEED = True
LOBFORCE_FORCE_HSPEED = 600
LOBFORCE_FORCE_VSPEED = -220
LOBFORCE_EXPLOSION_DURATION = 1
LOBFORCE_EXPLOSION_DAMAGE = 5

FORCE_RATE = 1
FORCE_AMMO_CONSUMPTION = 1
FORCE_DURATION = .7
FORCE_HSPEED = 500
FORCE_DAMAGE = 0
FORCE_ADD_PLAYER_SPEED = True
FORCE_FORCE_HSPEED = 100
FORCE_FORCE_VSPEED = -220

FORCEFORCE_RATE = 1
FORCEFORCE_AMMO_CONSUMPTION = 1
FORCEFORCE_DURATION = .8
FORCEFORCE_HSPEED = 500
FORCEFORCE_DAMAGE = 0
FORCEFORCE_ADD_PLAYER_SPEED = True
FORCEFORCE_FORCE_HSPEED = 300
FORCEFORCE_FORCE_VSPEED = -330
