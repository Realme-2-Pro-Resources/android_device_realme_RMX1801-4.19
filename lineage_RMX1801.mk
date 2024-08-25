#
# Copyright (C) 2020 The LineageOS Project
#
# SPDX-License-Identifier: Apache-2.0
#

# Inherit from those products. Most specific first.
$(call inherit-product, $(SRC_TARGET_DIR)/product/core_64_bit.mk)
$(call inherit-product, $(SRC_TARGET_DIR)/product/full_base_telephony.mk)
$(call inherit-product, $(SRC_TARGET_DIR)/product/product_launched_with_o_mr1.mk)

# Inherit some common LineageOS stuff
$(call inherit-product, vendor/lineage/config/common_full_phone.mk)

# Inherit from RMX1801 device
$(call inherit-product, $(LOCAL_PATH)/device.mk)

# Device identifier. This must come after all inclusions.
PRODUCT_NAME := lineage_RMX1801
PRODUCT_DEVICE := RMX1801
PRODUCT_BRAND := oppo
PRODUCT_MODEL := Realme 2 Pro
PRODUCT_MANUFACTURER := OPPO

PRODUCT_GMS_CLIENTID_BASE := android-oppo

PRODUCT_BUILD_PROP_OVERRIDES += \
    PRODUCT_DEVICE=RMX1801 \
    PRODUCT_NAME=RMX1801 \
    PRIVATE_BUILD_DESC="sdm660_64-user 10 QKQ1.191014.001 eng.root.20201016.161857 release-keys"

# Build fingerprint
BUILD_FINGERPRINT := "OPPO/RMX1801/RMX1801:10/QKQ1.191014.001/1602573502:user/release-keys"
