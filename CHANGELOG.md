# CHANGELOG

## v1.2.9 (2024-10-03)

### Build

* build: correct conditional for docker build on release only ([`753ca5a`](https://github.com/mbari-org/fastapi-yolov5/commit/753ca5a36fe0dc058ee9320c708381d658d49b5d))

### Performance

* perf: add GPU load if available ([`0e5d3e8`](https://github.com/mbari-org/fastapi-yolov5/commit/0e5d3e879cc9065099ded9b8485c83ccca5822c9))

## v1.2.8 (2024-05-21)

### Build

* build: switched release to python semantic release ([`b073439`](https://github.com/mbari-org/fastapi-yolov5/commit/b0734398998deeff91ebb45683d080510658b17e))

* build: switch to docker group ([`c65799c`](https://github.com/mbari-org/fastapi-yolov5/commit/c65799c8b98cd04a177987c26c28cb84e89be4e0))

### Fix

* fix: fake fix to trigger new release updated copyright ([`5a0ccc4`](https://github.com/mbari-org/fastapi-yolov5/commit/5a0ccc474c95fc31bcc193e6073cdc5d773d5759))

## v1.2.7 (2024-05-20)

### Fix

* fix: correct docker id for dev ops deployment ([`f81a637`](https://github.com/mbari-org/fastapi-yolov5/commit/f81a637d75469aabd2a7c026541693969c21a290))

## v1.2.6 (2024-05-16)

### Fix

* fix: security fixes per dependabot reports and pin cdk to work around https://github.com/aws/aws-cdk/issues/30241 in docker deploy ([`9b282f6`](https://github.com/mbari-org/fastapi-yolov5/commit/9b282f683f375702c13c22ba190159ed462053f9))

## v1.2.5 (2024-05-16)

### Fix

* fix: correct check for CDK_STACK_CONFIG ([`d2c062d`](https://github.com/mbari-org/fastapi-yolov5/commit/d2c062da71c4f25451d924ca46e1d37840e827a0))

## v1.2.4 (2024-05-16)

### Build

* build: correct release.yml formatting ([`57f6b2c`](https://github.com/mbari-org/fastapi-yolov5/commit/57f6b2c640c49eb8329ac21e980a925ff5db260b))

### Fix

* fix: correct pass through of yaml config through CDK_STACK_CONFIG variable ([`a914349`](https://github.com/mbari-org/fastapi-yolov5/commit/a91434987fd2ce9654ebb9783680c92dd184464c))

## v1.2.3 (2024-03-10)

### Build

* build: correct release.yml formatting ([`a08d646`](https://github.com/mbari-org/fastapi-yolov5/commit/a08d646e57393ceef4dc9481ccac63a1d9224b59))

* build: switch to codfish multiarch ([`64860c6`](https://github.com/mbari-org/fastapi-yolov5/commit/64860c66a2591a03936fa61d4e294726d76f2260))

* build: added more detail on cdk deploy ([`aa86867`](https://github.com/mbari-org/fastapi-yolov5/commit/aa86867aa1420ed9e6a5799b6dccaf9159af8be6))

* build: bumped version ([`e450d7f`](https://github.com/mbari-org/fastapi-yolov5/commit/e450d7f22fdbd3beeba26bc73fe5bf03827463b9))

### Documentation

* docs: minor edit ([`04b7949`](https://github.com/mbari-org/fastapi-yolov5/commit/04b7949467c318f0385560b05b8f62390367d03e))

* docs: updated instructions with correct path ([`9c94ab1`](https://github.com/mbari-org/fastapi-yolov5/commit/9c94ab183c6a8eae4ed5c28565bd2ad7a34b277c))

* docs: minor fix ([`e19790c`](https://github.com/mbari-org/fastapi-yolov5/commit/e19790c4c2e9aec1aeea13fbdfc0665ace7976f7))

* docs: minor update to fix links and remove live link ([`7cdb137`](https://github.com/mbari-org/fastapi-yolov5/commit/7cdb137b3704a2a957efdef378ebe6d2a36cb116))

### Fix

* fix: correct path for entrypoint ([`0e14994`](https://github.com/mbari-org/fastapi-yolov5/commit/0e149942cb3f1902897aa46330ca766bdd16ff62))

## v1.2.2 (2023-08-14)

### Build

* build: bumped version ([`57f6cbf`](https://github.com/mbari-org/fastapi-yolov5/commit/57f6cbfa5303ae91928834c7a2221a5fa1e1ef65))

### Fix

* fix: removed unused config ([`6f797c4`](https://github.com/mbari-org/fastapi-yolov5/commit/6f797c401accf8a0edf7ef4681728efa484a6db7))

## v1.2.1 (2023-08-14)

### Build

* build: bumped version ([`fc2ee43`](https://github.com/mbari-org/fastapi-yolov5/commit/fc2ee43f8ab654f937124380ea7ea5c3728cfd92))

### Fix

* fix: add in MODEL_WEIGHTS, MODEL_LABELS to cdk stack ([`8571930`](https://github.com/mbari-org/fastapi-yolov5/commit/8571930779f0d18041eb4feac5de427a8e5e1997))

## v1.2.0 (2023-08-14)

### Build

* build: bumped version ([`a42643a`](https://github.com/mbari-org/fastapi-yolov5/commit/a42643a52b93833f931d6d27c6a72dfe06ad5185))

### Feature

* feat: switch to float and renaming to better align with Pythia API ([`7ff01bb`](https://github.com/mbari-org/fastapi-yolov5/commit/7ff01bb4ca9982516032783261d75137e8fb567d))

## v1.1.0 (2023-08-14)

### Build

* build: bumped version ([`bd3e312`](https://github.com/mbari-org/fastapi-yolov5/commit/bd3e312745c9b469b830862ed0a788f99142033a))

### Documentation

* docs: minor update to dev notes ([`f9c3ccf`](https://github.com/mbari-org/fastapi-yolov5/commit/f9c3ccfdc71a05add9275866d478a74b74b91c84))

### Feature

* feat: support model checkpoint and labels with unique names ([`4065501`](https://github.com/mbari-org/fastapi-yolov5/commit/4065501f4286e8d15fb1952cdb51f85ba7e0e03d))

## v1.0.1 (2023-08-13)

### Build

* build: bumped version ([`d0bc0d1`](https://github.com/mbari-org/fastapi-yolov5/commit/d0bc0d17f7bea5bdbe17619ecb7cb1b6e818eafe))

### Documentation

* docs: added shields and minor update to description ([`8ae0dd1`](https://github.com/mbari-org/fastapi-yolov5/commit/8ae0dd1b741c8abc7e3f48d3fed0924f6e2e6c45))

### Fix

* fix: correct docker build for 3.10 as needed for current design ([`0608b74`](https://github.com/mbari-org/fastapi-yolov5/commit/0608b74cfa5ec83c89b45ddb35742e4b6f15b0db))

## v1.0.0 (2023-08-13)

### Build

* build: bumped version ([`052813f`](https://github.com/mbari-org/fastapi-yolov5/commit/052813f6b2abfee8825a61ef2bb1dd9fa8bad9c2))

* build: added version to cdk ([`5184cc0`](https://github.com/mbari-org/fastapi-yolov5/commit/5184cc01b740342be526c20e3629b66c8fc6f8ca))

* build: bumped version ([`c1bfe53`](https://github.com/mbari-org/fastapi-yolov5/commit/c1bfe5332bc783f758a5b96ba567f78a3b4e3ab0))

* build: bumped version ([`d3a83d5`](https://github.com/mbari-org/fastapi-yolov5/commit/d3a83d5c0db7ebb04034d673a0a84209f09c5641))

* build: bumped version ([`67d27ac`](https://github.com/mbari-org/fastapi-yolov5/commit/67d27acf14e65f2d64f4cbca180881e2054949fc))

* build: bumped version ([`b8f5ffa`](https://github.com/mbari-org/fastapi-yolov5/commit/b8f5ffa68f9cb9fe9406ac0fa67a4382402d5013))

* build: bumped version ([`f3ec212`](https://github.com/mbari-org/fastapi-yolov5/commit/f3ec212474d04bf1a79a25e577fe357bc0d65a81))

* build: bumped version ([`b041d86`](https://github.com/mbari-org/fastapi-yolov5/commit/b041d869a54b3caa85fa5cf83209222f4f0fc000))

* build: bumped version ([`760b825`](https://github.com/mbari-org/fastapi-yolov5/commit/760b82545e5a33073e80f37468dd1344d71f5837))

* build: bumped version ([`0ad5bd5`](https://github.com/mbari-org/fastapi-yolov5/commit/0ad5bd56fd40b0d6a7af12eb5de1aa30f77c8ee5))

* build: removed cdk out and move to package.json release ([`be17fbf`](https://github.com/mbari-org/fastapi-yolov5/commit/be17fbf722f5db210ccaaec23fef26c6acae3a25))

* build: switch to default health endpoint in load balancer, add conda env ([`d4bb0ab`](https://github.com/mbari-org/fastapi-yolov5/commit/d4bb0ab095ebe0b15972c7a770b43568c19f6ee5))

* build: correct context dir for docker build ([`791af4f`](https://github.com/mbari-org/fastapi-yolov5/commit/791af4f58db2dc52dadce9be43d2cc823bc57fff))

* build: fix branch in release ([`a72a2c0`](https://github.com/mbari-org/fastapi-yolov5/commit/a72a2c09a0178c6d5873e2f91652c623480e258b))

* build: fix branch in release ([`358c198`](https://github.com/mbari-org/fastapi-yolov5/commit/358c1980bccdadfdc9ab625fee0e509bbc36addb))

* build: fix dependency graph for release ([`839b21e`](https://github.com/mbari-org/fastapi-yolov5/commit/839b21ef7ee53a8843b2a0daf40d88bc0c293266))

* build: replace release ([`0bf5141`](https://github.com/mbari-org/fastapi-yolov5/commit/0bf5141556968ae65a3151c284d099f6c59784b1))

### Feature

* feat: Megadetector default, added description, output png instead of png, better pandas record handling and fixed ingress rules in CDK to force MBARI only access ([`70a9081`](https://github.com/mbari-org/fastapi-yolov5/commit/70a9081bf18594ecd763014c937faf9b7d8affa2))

* feat: switch to yaml config of stack ([`bc08b56`](https://github.com/mbari-org/fastapi-yolov5/commit/bc08b56597a00b9c9f35340b547a05a69406a419))

* feat: trigger release ([`e483963`](https://github.com/mbari-org/fastapi-yolov5/commit/e483963a5ebf9352602a7fdae19a80eb5c0cd398))

* feat: added secrets and cloud model load to cdk ([`6016e3c`](https://github.com/mbari-org/fastapi-yolov5/commit/6016e3c2f09ec6b4ba462b442059f3325a00d135))

* feat: added support for loading a custom model via env MODEL_PATH either local or S3 ([`59620b3`](https://github.com/mbari-org/fastapi-yolov5/commit/59620b310c96fc8e44d0010ce46ac358ea075823))

* feat: added MBARI security group and health check ([`7889a71`](https://github.com/mbari-org/fastapi-yolov5/commit/7889a714f80adfdd5be277c01b63ba6eb163f9c0))

* feat: initial commit ([`5fdae39`](https://github.com/mbari-org/fastapi-yolov5/commit/5fdae3908e6076844dd9bd5c5a1f15b34498a281))

### Fix

* fix: correct formatting of cdk.json ([`1bf3bfb`](https://github.com/mbari-org/fastapi-yolov5/commit/1bf3bfbce9cccec476d3466748d3980fac07e193))

* fix: entrypoint for docker image ([`042485b`](https://github.com/mbari-org/fastapi-yolov5/commit/042485b848a99011038045575bd717a15334d0dd))

### Performance

* perf: added autoscaling ([`58d3a60`](https://github.com/mbari-org/fastapi-yolov5/commit/58d3a60ffd011448381dae0681dd69e115c44e14))

* perf: reduce conf default to .01 ([`49ee785`](https://github.com/mbari-org/fastapi-yolov5/commit/49ee7856c7ce6367f8482a9df3359fd2ab328d46))

* perf: reduce  conf to 0.1 ([`ad1dcb8`](https://github.com/mbari-org/fastapi-yolov5/commit/ad1dcb86d48bcf1a136eb565ee36d9179088acdf))

### Unknown

* Initial commit ([`53f77f0`](https://github.com/mbari-org/fastapi-yolov5/commit/53f77f062bcaa71ea6c6077b0706c2813842b865))
