const _findBasePath = (scope) => {
  if (scope.upperScope) return _findBasePath(scope.upperScope);
  return scope.basepath;
}

module.exports = _findBasePath;
