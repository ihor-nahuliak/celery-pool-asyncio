# Changelog

## [0.1.9]
- Large rework of `await AsyncResult.get()`
    - Works much better than earlier, but it's crap still
    - Added outnumber of monkey-patches
- Fixed race condition on first microseconds of pool shutdown

## [0.1.8]
- Cleanup tracer, use celery.app.trace namespase where it possible

## [0.1.7]
- Refactor monkey, split it
- Move patch_send_task to own function
- Add patch_result_get to await AsyncResult.get

## [0.1.6]
- Avoid building trace twice
- Also this small performance optimization fixed AsyncResult.get

## [0.1.5]
- Fix graceful shutdown

## [0.1.4]
- Fix monkey: another function must be patched

## [0.1.3]
- Add changelog
- Append documentation

## [0.1.2]
- Add monkey patcher to make brocker IO operations nonblocking

## [0.1.1]
- Refactor code
- Fix found errors

## [0.1.0]
- Initial commit
