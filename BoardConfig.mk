#
# Copyright (C) 2025 The LineageOS Project
#
# SPDX-License-Identifier: Apache-2.0
#

# Inherit from sdm660-common
include device/oppo/sdm660-common/BoardConfigCommon.mk

# Inherit the proprietary files
include vendor/realme/RMX1801/BoardConfigVendor.mk

DEVICE_PATH := device/realme/RMX1801

# Asserts
TARGET_OTA_ASSERT_DEVICE := RMX1801,RMX1803,RMX1807

# Display
TARGET_SCREEN_HEIGHT := 2160
TARGET_SCREEN_WIDTH := 1080

# Partitions
BOARD_CACHEIMAGE_PARTITION_SIZE := 260014080
BOARD_SYSTEMIMAGE_PARTITION_SIZE := 5460574208
BOARD_USERDATAIMAGE_PARTITION_SIZE := 56933465600
BOARD_VENDORIMAGE_PARTITION_SIZE := 1610612736
