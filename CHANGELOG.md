# Changelog

## [2.1.0](https://github.com/adrighem/pp-manager/compare/v2.0.0...v2.1.0) (2026-05-10)


### Features

* add 'Repo' button to plugin cards ([8cd1389](https://github.com/adrighem/pp-manager/commit/8cd138955799bc793facd69cb81763e06334970e))
* add new Domoticz Python plugins ([c67a813](https://github.com/adrighem/pp-manager/commit/c67a8135c3c1d2ee9822acf9895ecbf15b29cb88))
* add new Domoticz Python plugins ([03b13e4](https://github.com/adrighem/pp-manager/commit/03b13e4dcb92737356fc248a6298cfbb07de8a3b))
* add search filter and installed-only toggle to dashboard ([7e25c1f](https://github.com/adrighem/pp-manager/commit/7e25c1fd8e0e96bd7d866fc5b6cbe62794227ad5))
* implement device bus API and custom HTML dashboard ([01ca5ef](https://github.com/adrighem/pp-manager/commit/01ca5efb29232a5619bb202059acff1859d00261))
* improve custom UI autoinstall logic ([5951e29](https://github.com/adrighem/pp-manager/commit/5951e2907732723409460c0276a3e303535ddb6d))
* make security scanner smarter by ignoring private IPs and targeting high-risk subprocess calls ([283e0b6](https://github.com/adrighem/pp-manager/commit/283e0b635d0c55e209209fa05c06d00164187b32))
* overhaul monthly scan to sync full registry and show 'last updated' in UI ([6cbf85e](https://github.com/adrighem/pp-manager/commit/6cbf85efb4583dd275b26eff944ed4f16192db7b))


### Bug Fixes

* add cache busters and absolute paths to API calls ([e74bda8](https://github.com/adrighem/pp-manager/commit/e74bda8ecd7aefe0cd5b01b2effe1dcfc377c5e9))
* call init directly to support SPA injection ([f6da725](https://github.com/adrighem/pp-manager/commit/f6da725bd1f3316c865180c11fcfe1b7b0d32747))
* echo back tx_id in API responses to unblock frontend polling ([f7f1476](https://github.com/adrighem/pp-manager/commit/f7f1476e6cc9f711d716953b31e2108d84360d88))
* ignore version-like strings that look like IPs in User Agents ([08c386b](https://github.com/adrighem/pp-manager/commit/08c386b81ef27620efe3ba8d73c42c8748a8a179))
* refactor HTML to snippet and improve SPA init logic ([bab35ca](https://github.com/adrighem/pp-manager/commit/bab35caa6bcdeb0c19ee01a8ada2f7631209d787))
* refactor Repo button to simple anchor link ([2821b24](https://github.com/adrighem/pp-manager/commit/2821b24af9085886c622e98466e732751153291a))
* refine scanner to ignore version-like IPs and safe json.loads calls ([6fcb4b0](https://github.com/adrighem/pp-manager/commit/6fcb4b034ab8279a11210fee531f4d4ffdeceb00))
* resolve NameError for datetime and json imports ([4a6f748](https://github.com/adrighem/pp-manager/commit/4a6f748a0ac517bc444fb484a650c317563331b4))
* resolve NameError for home_folder in installDependencies ([15e8709](https://github.com/adrighem/pp-manager/commit/15e87091f24e0a6cd0829267a161da5dd12a5d1b))
* resolve XML encoding issue in plugin generator ([b48c517](https://github.com/adrighem/pp-manager/commit/b48c5172dc8bee841415e6b9edc27411e20b93e6))
* restore method indentation for is_private_ip ([540627c](https://github.com/adrighem/pp-manager/commit/540627cbb3038cd0b0f79b0328fcacbf6aad8005))
* revert to relative paths for subpath support ([facdfa2](https://github.com/adrighem/pp-manager/commit/facdfa254825c1096fe29d2377c7502d46e85761))
* update polling to use modern getdevices API syntax ([5c5b9c3](https://github.com/adrighem/pp-manager/commit/5c5b9c3089c8b62ba0a9803727bb9a7909c7c183))


### Documentation

* rename dashboard screenshot and update README with new UI instructions ([3130628](https://github.com/adrighem/pp-manager/commit/3130628212095524f18c3f67ea3e8ce5debbf8a1))

## [2.0.0](https://github.com/adrighem/pp-manager/compare/v1.5.47...v2.0.0) (2026-04-06)


### ⚠ BREAKING CHANGES

* configure release-please to start at 2.0.0 and update plugin files

### Features

* add monthly github action to discover domoticz plugins ([a3dd3df](https://github.com/adrighem/pp-manager/commit/a3dd3dff5e13045ebcf0bf60e67024573c7a7c30))
* bump version to 2.0.0 and add release-please workflow ([dce185b](https://github.com/adrighem/pp-manager/commit/dce185b34bb9280008a5aea551f94e6487ad862c))
* configure release-please to start at 2.0.0 and update plugin files ([d24f894](https://github.com/adrighem/pp-manager/commit/d24f894cad3f6aa4acd71d924be7046367fa69b6))


### Documentation

* update forum link in README ([871a666](https://github.com/adrighem/pp-manager/commit/871a666467a13ec764f927cd3ecbb3365560b1cd))
