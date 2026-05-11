# Changelog

## [2.2.1](https://github.com/adrighem/PyPluginStore/compare/v2.2.0...v2.2.1) (2026-05-11)


### Bug Fixes

* correct capitalization in javascript getElementById ([3c55090](https://github.com/adrighem/PyPluginStore/commit/3c550904126cd31880ce9aa1a98437043812d300))
* remove pp-manager from registry and ignore in monthly scans ([5a7003a](https://github.com/adrighem/PyPluginStore/commit/5a7003a36a1dede054adb13383e86cc7aa9faa88))
* revert plugin key to PP-MANAGER for hardware backward compatibility and remove legacy UI ([68bfbc7](https://github.com/adrighem/PyPluginStore/commit/68bfbc7a807b16e4abae87b4bf7f3d1da31fde07))


### Documentation

* update store screenshot with new PyPluginStore UI ([1f61e6f](https://github.com/adrighem/PyPluginStore/commit/1f61e6f840afee27af928b88e29302d4169d0d88))

## [2.2.0](https://github.com/adrighem/PyPluginStore/compare/v2.1.0...v2.2.0) (2026-05-11)


### Features

* add KPN Experia v10 plugin to registry ([290a08e](https://github.com/adrighem/PyPluginStore/commit/290a08ed7470f415f76a4b4910b4a7e45230d78b))


### Bug Fixes

* revert original repo name and url in fork note and registry ([ad0b51d](https://github.com/adrighem/PyPluginStore/commit/ad0b51df380634743ceeb723e19a114a261f1ee7))

## [2.1.0](https://github.com/adrighem/PyPluginStore/compare/v2.0.0...v2.1.0) (2026-05-10)


### Features

* add 'Repo' button to plugin cards ([8cd1389](https://github.com/adrighem/PyPluginStore/commit/8cd138955799bc793facd69cb81763e06334970e))
* add new Domoticz Python plugins ([c67a813](https://github.com/adrighem/PyPluginStore/commit/c67a8135c3c1d2ee9822acf9895ecbf15b29cb88))
* add new Domoticz Python plugins ([03b13e4](https://github.com/adrighem/PyPluginStore/commit/03b13e4dcb92737356fc248a6298cfbb07de8a3b))
* add search filter and installed-only toggle to dashboard ([7e25c1f](https://github.com/adrighem/PyPluginStore/commit/7e25c1fd8e0e96bd7d866fc5b6cbe62794227ad5))
* implement device bus API and custom HTML dashboard ([01ca5ef](https://github.com/adrighem/PyPluginStore/commit/01ca5efb29232a5619bb202059acff1859d00261))
* improve custom UI autoinstall logic ([5951e29](https://github.com/adrighem/PyPluginStore/commit/5951e2907732723409460c0276a3e303535ddb6d))
* make security scanner smarter by ignoring private IPs and targeting high-risk subprocess calls ([283e0b6](https://github.com/adrighem/PyPluginStore/commit/283e0b635d0c55e209209fa05c06d00164187b32))
* overhaul monthly scan to sync full registry and show 'last updated' in UI ([6cbf85e](https://github.com/adrighem/PyPluginStore/commit/6cbf85efb4583dd275b26eff944ed4f16192db7b))


### Bug Fixes

* add cache busters and absolute paths to API calls ([e74bda8](https://github.com/adrighem/PyPluginStore/commit/e74bda8ecd7aefe0cd5b01b2effe1dcfc377c5e9))
* call init directly to support SPA injection ([f6da725](https://github.com/adrighem/PyPluginStore/commit/f6da725bd1f3316c865180c11fcfe1b7b0d32747))
* echo back tx_id in API responses to unblock frontend polling ([f7f1476](https://github.com/adrighem/PyPluginStore/commit/f7f1476e6cc9f711d716953b31e2108d84360d88))
* ignore version-like strings that look like IPs in User Agents ([08c386b](https://github.com/adrighem/PyPluginStore/commit/08c386b81ef27620efe3ba8d73c42c8748a8a179))
* refactor HTML to snippet and improve SPA init logic ([bab35ca](https://github.com/adrighem/PyPluginStore/commit/bab35caa6bcdeb0c19ee01a8ada2f7631209d787))
* refactor Repo button to simple anchor link ([2821b24](https://github.com/adrighem/PyPluginStore/commit/2821b24af9085886c622e98466e732751153291a))
* refine scanner to ignore version-like IPs and safe json.loads calls ([6fcb4b0](https://github.com/adrighem/PyPluginStore/commit/6fcb4b034ab8279a11210fee531f4d4ffdeceb00))
* resolve NameError for datetime and json imports ([4a6f748](https://github.com/adrighem/PyPluginStore/commit/4a6f748a0ac517bc444fb484a650c317563331b4))
* resolve NameError for home_folder in installDependencies ([15e8709](https://github.com/adrighem/PyPluginStore/commit/15e87091f24e0a6cd0829267a161da5dd12a5d1b))
* resolve XML encoding issue in plugin generator ([b48c517](https://github.com/adrighem/PyPluginStore/commit/b48c5172dc8bee841415e6b9edc27411e20b93e6))
* restore method indentation for is_private_ip ([540627c](https://github.com/adrighem/PyPluginStore/commit/540627cbb3038cd0b0f79b0328fcacbf6aad8005))
* revert to relative paths for subpath support ([facdfa2](https://github.com/adrighem/PyPluginStore/commit/facdfa254825c1096fe29d2377c7502d46e85761))
* update polling to use modern getdevices API syntax ([5c5b9c3](https://github.com/adrighem/PyPluginStore/commit/5c5b9c3089c8b62ba0a9803727bb9a7909c7c183))


### Documentation

* rename dashboard screenshot and update README with new UI instructions ([3130628](https://github.com/adrighem/PyPluginStore/commit/3130628212095524f18c3f67ea3e8ce5debbf8a1))

## [2.0.0](https://github.com/adrighem/PyPluginStore/compare/v1.5.47...v2.0.0) (2026-04-06)


### ⚠ BREAKING CHANGES

* configure release-please to start at 2.0.0 and update plugin files

### Features

* add monthly github action to discover domoticz plugins ([a3dd3df](https://github.com/adrighem/PyPluginStore/commit/a3dd3dff5e13045ebcf0bf60e67024573c7a7c30))
* bump version to 2.0.0 and add release-please workflow ([dce185b](https://github.com/adrighem/PyPluginStore/commit/dce185b34bb9280008a5aea551f94e6487ad862c))
* configure release-please to start at 2.0.0 and update plugin files ([d24f894](https://github.com/adrighem/PyPluginStore/commit/d24f894cad3f6aa4acd71d924be7046367fa69b6))


### Documentation

* update forum link in README ([871a666](https://github.com/adrighem/PyPluginStore/commit/871a666467a13ec764f927cd3ecbb3365560b1cd))
