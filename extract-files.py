#!/usr/bin/env -S PYTHONPATH=../../../tools/extract-utils python3
#
# SPDX-FileCopyrightText: 2024 The LineageOS Project
# SPDX-License-Identifier: Apache-2.0
#

import extract_utils.tools

extract_utils.tools.DEFAULT_PATCHELF_VERSION = '0_17_2'

from extract_utils.fixups_blob import (
    blob_fixup,
    blob_fixups_user_type,
)
from extract_utils.fixups_lib import (
    lib_fixup_remove,
    lib_fixups,
    lib_fixups_user_type,
)
from extract_utils.main import (
    ExtractUtils,
    ExtractUtilsModule,
)

namespace_imports = [
    'device/realme/RMX1801',
    'hardware/qcom-caf/sdm660',
    'hardware/qcom-caf/wlan',
    'hardware/oppo',
    'vendor/qcom/opensource/commonsys/display',
    'vendor/qcom/opensource/dataservices',
    'vendor/qcom/opensource/display',
]

def lib_fixup_vendor_suffix(lib: str, partition: str, *args, **kwargs):
    return f'{lib}_{partition}' if partition == 'vendor' else None

lib_fixups: lib_fixups_user_type = {
    **lib_fixups,
    (
        'com.qualcomm.qti.dpm.api@1.0',
        'vendor.qti.hardware.fm@1.0',
        'vendor.qti.imsrtpservice@3.0',
    ): lib_fixup_vendor_suffix,
    (
    ): lib_fixup_remove,
}

blob_fixups: blob_fixups_user_type = {
    'vendor/etc/init/android.hardware.gnss@2.1-service-qti.rc': blob_fixup()
        .regex_replace('    disabled', '    #disabled'),
    'vendor/lib/hw/camera.sdm660.so': blob_fixup()
        .binary_regex_replace(b'/system/etc/camera/', b'/vendor/etc/camera/')
        .sig_replace('30 68 4f f4 51 73 c1 68 d0 e9 0d 20', '30 68 4f f4 51 73 c1 68 d0 e9 12 20')
        .sig_replace('31 68 08 9a 00 26 49 6b cb e9', '31 68 08 9a 00 26 89 6c cb e9'),
    'vendor/lib/libdepthmap.so': blob_fixup()
        .clear_symbol_version('remote_handle_close')
        .clear_symbol_version('remote_handle_invoke')
        .clear_symbol_version('remote_handle_open')
        .replace_needed('libstdc++.so', 'libstdc++_vendor.so'),
    'vendor/lib/libmmcamera_faceproc.so': blob_fixup()
        .clear_symbol_version('__aeabi_memcpy')
        .clear_symbol_version('__aeabi_memset')
        .clear_symbol_version('__gnu_Unwind_Find_exidx'),
    'vendor/lib/libmmcamera_hdr_gb_lib.so': blob_fixup()
        .add_needed("liblog.so")
        .replace_needed('libstdc++.so', 'libstdc++_vendor.so'),
    'vendor/lib/libVDBlurlessAPI_v2.so': blob_fixup()
        .clear_symbol_version('remote_handle64_close')
        .clear_symbol_version('remote_handle64_invoke')
        .clear_symbol_version('remote_handle64_open'),
    'vendor/lib/sensors.ssc.so': blob_fixup()
        .sig_replace('73 08 68 28 21', '73 08 68 f0 21')
        .sig_replace('6e 28 74', 'f0 28 74')
        .sig_replace('74 d1 9a f8 09 00', '74 d1 00 f0 46 b8')
        .sig_replace('08 28 00 f2 a3 80', '08 28 00 f2 6b 80'),
    'vendor/lib/soundfx/libswdap.so': blob_fixup()
        .sig_replace('2d e9 f0 4f b5 b0 83 46', '01 20 70 47 00 bf 00 bf'),
    'vendor/lib64/libqmiservices.so': blob_fixup()
        .sig_replace(
            '0B 00 00 00 23 00 0D 00 00 00 24 00 0F 00 00 00 25 00 11 00 00 00 26 00 15 00 00 00 27 00 17 00 16 00 28 00 19 00',
            '0B 00 00 00 23 00 0D 00 00 00 24 00 0F 00 00 00 25 00 55 00 04 00 26 00 15 00 00 00 27 00 17 00 16 00 28 00 19 00'
        ),
    'vendor/lib64/libril-qc-hal-qmi.so': blob_fixup()
        .sig_replace(
            '06 A6 8E 52 E3 C7 41 B9 E4 BF 40 F9 E5 77 41 B9 42 7F 35 94 E0 EB 01 B9 E0 EB 41 B9',
            '06 A6 8E 52 E3 C7 41 B9 E4 BF 40 F9 E5 77 41 B9 DC F3 EE 97 E0 EB 01 B9 E0 EB 41 B9'
        )
        .sig_replace(
            'E0 02 80 52 CE 80 46 94 C0 04 00 34 D8 8C 46 94 E0 3B 00 B9 E8 3B 40 B9 1F 01 00 71 E8 B7 9F 1A 08 04 00 37',
            'E0 02 80 52 CE 80 46 94 C0 04 00 34 D8 8C 46 94 E0 3B 00 B9 E8 3B 40 B9 1F 01 00 71 E8 B7 9F 1A 20 00 00 14'
        )
        .sig_replace(
            '20 BC FF B0 00 E8 17 91 84 80 46 94 E0 17 00 F9 86 80 46 94 E0 13 00 F9 88 80 46 94 E1 03 00 2A 26 7C 40 93 E6 0F 00 F9 73 FF FF 97 E8 3B 40 B9 A9 00 80 52 E0 0B 00 F9 E0 03 09 2A 21 BE FF 90 21 90 2D 91 A2 BF FF F0 42 48 27 91',
            'FF 03 01 D1 FD 7B 03 A9 FD C3 00 91 E0 13 00 A9 E5 1B 01 A9 39 40 FC 97 08 04 00 11 E8 83 00 39 E0 03 40 F9 A1 04 80 52 E2 83 00 91 23 00 80 52 E4 07 40 F9 E5 13 40 B9 E6 1B 40 B9 CD FF FF 97 FD 7B 43 A9 FF 03 01 91 C0 03 5F D6'
        ),
    'vendor/lib64/sensors.ssc.so': blob_fixup()
        .sig_replace('39 28 00 40 f9 09 05 80 52', '39 28 00 40 f9 09 1e 80 52')
        .sig_replace('1f b9 01 71 a1', '1f c1 03 71 a1' )
        .sig_replace('54 a8 02 16 8b 08 25 40 39 a8', '54 4a 00 00 14 08 25 40 39 a8')
        .sig_replace('7f b8 01 71 01 0b 00 54', '7f b8 01 71 a1 07 00 54'),
    'vendor/lib64/soundfx/libswdap.so': blob_fixup()
        .sig_replace('ff 83 04 d1 fd 7b 0e a9', '20 00 80 52 c0 03 5f d6'),
    (
        'vendor/lib/libthread_blur.so',
        'vendor/lib/libVDDualCameraBlurlessAPI.so',
        'vendor/lib/libVDSuperPhotoAPI.so',
    ): blob_fixup()
        .clear_symbol_version('remote_handle_close')
        .clear_symbol_version('remote_handle_invoke')
        .clear_symbol_version('remote_handle_open'),
    (
        'system_ext/lib64/lib-imscamera.so',
        'system_ext/lib64/lib-imsvideocodec.so',
    ): blob_fixup()
        .add_needed('libgui_shim.so'),
    (
        'vendor/lib/libmmcamera_pdaf.so',
        'vendor/lib/libmmcamera_pdafcamif.so',
        'vendor/lib/libmmcamera_tintless_bg_pca_algo.so',
        'vendor/lib64/libmmcamera_tintless_bg_pca_algo.so',
    ): blob_fixup()
        .add_needed("liblog.so"),
    (
        'vendor/lib/libarcvs.dep.so',
        'vendor/lib/libmmcamera2_sensor_modules.so',
        'vendor/lib/libmmcamera_interface.so',
    ): blob_fixup()
        .binary_regex_replace(b'/system/etc/camera/', b'/vendor/etc/camera/'),
    (
        'vendor/lib/libPerfectlyClearCrux.so',
        'vendor/lib/libSonyIMX376RmscLibrary.so',
        'vendor/lib/libSonyIMX519PdafLibrary.so',
        'vendor/lib/libarcsoft_dualcam_bokeh_api.so',
        'vendor/lib/libarcsoft_dualcam_refocus.so',
        'vendor/lib/libarcsoft_dualcam_refocus_left.so',
        'vendor/lib/libarcsoft_dualcam_refocus_preview.so',
        'vendor/lib/libarcsoft_dualcam_refocus_right.so',
        'vendor/lib/libarcsoft_smart_denoise.so',
        'vendor/lib/libfilter.so',
    ): blob_fixup()
        .replace_needed('libstdc++.so', 'libstdc++_vendor.so'),
}  # fmt: skip

module = ExtractUtilsModule(
    'RMX1801',
    'realme',
    blob_fixups=blob_fixups,
    lib_fixups=lib_fixups,
    namespace_imports=namespace_imports,
)

if __name__ == '__main__':
    utils = ExtractUtils.device(module)
    utils.run()
