#
# Copyright (C) 2025 The LineageOS Project
#
# SPDX-License-Identifier: Apache-2.0
#

# Inherit from sdm660-common
$(call inherit-product, device/oppo/sdm660-common/common.mk)

# Inherit the proprietary files
$(call inherit-product, vendor/realme/RMX1801/RMX1801-vendor.mk)

# Overlays
PRODUCT_PACKAGES += \
    FrameworkResOverlayRMX1801

# Soong namespaces
PRODUCT_SOONG_NAMESPACES += \
    $(LOCAL_PATH)
