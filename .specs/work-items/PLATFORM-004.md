---
item: android-shell-and-apk-gate
module: platform
status: draft
priority: medium
depends_on: [CHECKIN-002]
---

# CHANGE

Scaffold the Capacitor Android shell (@capacitor/android + `cap add android`) and turn the APK build into a required, containerized per-PR CI gate (`gradlew assembleDebug`).

## WHY

ADR-006 requires every PR to pass unit + e2e + APK build. On the empty scaffold there is no Android project, so the APK gate is deferred (apk.yml is manual-only) until a real screen exists to package.

## SCOPE

### Included

- add @capacitor/android and generate the android/ project
- containerized APK build (Android SDK image) producing a debug APK
- flip apk.yml to run on pull_request/push as a required gate
- upload the APK artifact

### Excluded

- signing/release builds and store publishing

## ACCEPTANCE

### AC-001

Given a pull request

When CI runs

Then the APK job assembles a debug APK and uploads it as an artifact.

## NOTES

Depends on CHECKIN-002 so there is a real Home screen to package.
