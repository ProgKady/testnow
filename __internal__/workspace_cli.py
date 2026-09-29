import json
import sys

import workspace_cli


def main(argv=None):
    argv = list(sys.argv[1:] if argv is None else argv)
    if not argv:
        print(json.dumps({"ok": False, "error": "missing command"}, ensure_ascii=False))
        return 1
    command = argv.pop(0)
    payload = {}
    if argv:
        try:
            payload = json.loads(argv[0]) if argv[0] else {}
        except Exception as e:
            print(json.dumps({"ok": False, "error": f"invalid json payload: {e}"}, ensure_ascii=False))
            return 1
    try:
        result = workspace_cli.run(command, **payload)
    except Exception as e:
        print(json.dumps({"ok": False, "command": command, "error": str(e)}, ensure_ascii=False))
        return 1
    print(json.dumps(result, ensure_ascii=False))
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
