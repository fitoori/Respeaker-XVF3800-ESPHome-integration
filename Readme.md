# ESPHome components and example config for Respeaker XVF3800

# ATTENTION! Early alpha, use on your own risk!

## External components setup

Use the `external_components` entry below when you are pulling the components from
GitHub. Make sure you reference the repository that actually ships the
`components/` directory (older forks may not), otherwise ESPHome will report that
the components folder is missing.

```yaml
external_components:
  - source:
      type: git
      url: https://github.com/formatBCE/Respeaker-XVF3800-ESPHome-integration
      ref: main
    components:
      - respeaker_xvf3800
      - aic3104
```
