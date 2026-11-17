#!/usr/bin/env bash
# 使い方:
#   ./run.sh 447          contest_447 の default_folders を全部実行
#   ./run.sh 447 d        contest_447 の d を実行
#   ./run.sh 447 d -p java  言語指定 (python/java/rust)
#   ./run.sh -h           このヘルプを表示 (引数なしでも表示)
set -euo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
ABC="$ROOT/atcoder/ABC"
cd "$ROOT"

usage() {
  sed -n '2,/^set -/{/^set -/!s/^# \{0,1\}//p}' "${BASH_SOURCE[0]}"
}

if [[ $# -eq 0 || "${1:-}" == "-h" || "${1:-}" == "--help" ]]; then
  usage
  exit 0
fi

contest="$1"
problem="${2:-}"
shift $(( $# > 2 ? 2 : $# )) || true

args=(-d "$ABC/contest_${contest#contest_}")
[[ -n "$problem" ]] && args+=(-t "$problem")

exec uv run python "$ABC/scripts/run.py" "${args[@]}" "$@"
