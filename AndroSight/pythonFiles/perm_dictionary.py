permission_dict = {
    "android.permission.GET_ACCOUNTS": "  This permission allows access to the user's accounts (It may have privacy implications, but whether it constitutes a vulnerability depends on how it is used in your specific application.)",
    "android.permission.MANAGE_ACCOUNTS": "  This permission provides the ability to manage accounts on the device. (its vulnerability status depends on the context and the potential risks associated with the account management functionality in your application.)",
    "android.permission.PACKAGE_USAGE_STATS": "  This permission grants access to the user's package usage statistics. It is typically used by monitoring or analytics applications. (Not a vulnerability)",
    "android.permission.ACCESS_WIFI_STATE": "  This permission is related to Wi-Fi connectivity. While it may have security implications if misused, its generally not considered vulnerabilities in itmselve.",
    "android.permission.CHANGE_WIFI_STATE": "  This permission is related to Wi-Fi connectivity. While it may have security implications if misused, its generally not considered vulnerabilities in itmselve.",
    "android.permission.INTERNET": "  This permission allows network access, which is essential for most applications. However, it should be implemented securely to mitigate potential vulnerabilities, such as protecting against unauthorized data access or network attacks.",
    "android.permission.RECEIVE_BOOT_COMPLETED": "  This permission allows the app to receive a notification when the device finishes booting. While it has certain implications, it is typically not considered a vulnerability on its own.",
    "android.permission.ACCESS_NETWORK_STATE": "  This permission enables access to information about the device's network connectivity. It is generally not considered a vulnerability but should be handled securely to prevent unauthorized access or data leakage.",
    "android.permission.FOREGROUND_SERVICE": "  This permission grants the ability to run foreground services. It is an important permission for certain app functionalities but needs to be implemented securely to avoid potential vulnerabilities, such as misuse of background processes or excessive resource consumption.",
    "android.permission.READ_EXTERNAL_STORAGE": "  This permission provide access to external storage (e.g., SD card). it may have security implications if used improperly, such as unauthorized access to sensitive files. Proper validation and security measures should be implemented to prevent vulnerabilities.",
    "android.permission.WRITE_EXTERNAL_STORAGE":"  This permission provide access to external storage (e.g., SD card). it may have security implications if used improperly, such as unauthorized access to sensitive files. Proper validation and security measures should be implemented to prevent vulnerabilities.",
    "android.permission.REQUEST_PASSWORD_COMPLEXITY": "  This permission is related to requesting password complexity. Its vulnerability status depends on how it is used in your specific application and the potential risks associated with password management.",
    "android.permission.ACCESS_FINE_LOCATION": "  This permission allows access to precise location information. It may have privacy implications, but whether it constitutes a vulnerability depends on the specific implementation and the potential risks associated with location data handling.",
    "android.permission.QUERY_ALL_PACKAGES": "  This permission grants access to information about installed apps on the device. It may have privacy implications, but whether it poses a vulnerability depends on the specific functionality and potential risks associated with querying app packages.)"
}


component_dict = {
    # "Activity"
        "com.afwsamples.testdpc.PolicyManagementActivity": "Policy Management ",
        "com.afwsamples.testdpc.SetupManagementActivity": "Setup Management ",
        "com.afwsamples.testdpc.AddAccountActivity": "Add Account ",
        "com.afwsamples.testdpc.FinalizeActivity": "Finalize ",
        "com.afwsamples.testdpc.cosu.EnableCosuActivity": "Enable COSU ",
        "com.afwsamples.testdpc.policy.locktask.KioskModeActivity": "Kiosk Mode ",
        "com.afwsamples.testdpc.provision.GetProvisioningModeActivity": "Get Provisioning Mode ",
        "com.afwsamples.testdpc.provision.ProvisioningSuccessActivity": "Provisioning Success ",
        "com.afwsamples.testdpc.WorkPolicyInfoActivity": "Work Policy Info ",
        "com.afwsamples.testdpc.provision.DpcLoginActivity": "   Device Policy Controller (DPC) login",
    #"Service"
        "com.afwsamples.testdpc.policy.resetpassword.ResetPasswordService": "Reset Password (Potential vulnerability)\n - This service allows resetting the password and might be exploited by malicious users to gain unauthorized access.",
        "com.afwsamples.testdpc.profilepolicy.apprestrictions.AppRestrictionsProxy": "App Restrictions Proxy (Not a vulnerability)",
        "com.afwsamples.testdpc.comp.ProfileOwnerService": "Profile Owner (Not a vulnerability)",
        "com.afwsamples.testdpc.comp.DeviceOwnerService": "Device Owner (Not a vulnerability)",
        "com.afwsamples.testdpc.DeviceAdminService": "Device Admin (Not a vulnerability)",
        "com.afwsamples.testdpc.feedback.AppStatesService": "App States (Not a vulnerability)",

    #"Receiver"
        "com.afwsamples.testdpc.DeviceAdminReceiver": "Device Admin ",
        "com.afwsamples.testdpc.DelegatedAdminReceiver": "Delegated Admin ",
        "com.afwsamples.testdpc.BootReceiver": "Boot ",
        "com.afwsamples.testdpc.policy.resetpassword.ResetPasswordService$LockedBootCompletedReceiver": "Locked Boot Completed (Potential vulnerability)\n - This receiver listens for locked boot completed events and might be exploited by malicious applications to perform unauthorized actions during device startup.",
    #"Provider"
        "androidx.core.content.FileProvider": "File Provider ",
        "com.afwsamples.testdpc.UserIconContentProvider": "User Icon Content ",
        "androidx.lifecycle.ProcessLifecycleOwnerInitializer": "Process Lifecycle Owner "

}