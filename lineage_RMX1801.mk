#
# Copyright (C) 2025 The LineageOS Project
#
# SPDX-License-Identifier: Apache-2.0
#

# Inherit from those products. Most specific first.
$(call inherit-product, $(SRC_TARGET_DIR)/product/core_64_bit.mk)
$(call inherit-product, $(SRC_TARGET_DIR)/product/full_base_telephony.mk)

# Inherit some common Lineage stuff.
$(call inherit-product, vendor/lineage/config/common_full_phone.mk)

# Inherit from RMX1801 device
$(call inherit-product, device/realme/RMX1801/device.mk)

PRODUCT_DEVICE := RMX1801
PRODUCT_NAME := lineage_RMX1801
PRODUCT_BRAND := OPPO
PRODUCT_MODEL := Realme 2 Pro
PRODUCT_MANUFACTURER := OPPO

PRODUCT_GMS_CLIENTID_BASE := android-oppo

PRODUCT_BUILD_PROP_OVERRIDES += \
    BuildDesc="sdm660_64-user 10 QKQ1.191014.001 eng.root.20201016.161857 release-keys" \
    BuildFingerprint=OPPO/RMX1801/RMX1801:10/QKQ1.191014.001/1602573502:user/release-keys
