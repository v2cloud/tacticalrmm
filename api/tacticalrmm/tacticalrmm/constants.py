from enum import Enum

from django.db import models


class MeshAgentIdent(Enum):
    WIN32 = 3
    WIN64 = 4
    LINUX32 = 5
    LINUX64 = 6
    LINUX_ARM_64 = 26
    LINUX_ARM_HF = 25

    def __str__(self):
        return str(self.value)


CORESETTINGS_CACHE_KEY = "core_settings"
ROLE_CACHE_PREFIX = "role_"


class ScriptShell(models.TextChoices):
    POWERSHELL = "powershell", "Powershell"
    CMD = "cmd", "Batch (CMD)"
    PYTHON = "python", "Python"
    SHELL = "shell", "Shell"


class ScriptType(models.TextChoices):
    USER_DEFINED = "userdefined", "User Defined"
    BUILT_IN = "builtin", "Built In"


class EvtLogNames(models.TextChoices):
    APPLICATION = "Application", "Application"
    SYSTEM = "System", "System"
    SECURITY = "Security", "Security"


class EvtLogTypes(models.TextChoices):
    INFO = "INFO", "Information"
    WARNING = "WARNING", "Warning"
    ERROR = "ERROR", "Error"
    AUDIT_SUCCESS = "AUDIT_SUCCESS", "Success Audit"
    AUDIT_FAILURE = "AUDIT_FAILURE", "Failure Audit"


class EvtLogFailWhen(models.TextChoices):
    CONTAINS = "contains", "Log contains"
    NOT_CONTAINS = "not_contains", "Log does not contain"


class CheckStatus(models.TextChoices):
    PASSING = "passing", "Passing"
    FAILING = "failing", "Failing"
    PENDING = "pending", "Pending"


class PAStatus(models.TextChoices):
    PENDING = "pending", "Pending"
    COMPLETED = "completed", "Completed"


class PAAction(models.TextChoices):
    SCHED_REBOOT = "schedreboot", "Scheduled Reboot"
    AGENT_UPDATE = "agentupdate", "Agent Update"
    CHOCO_INSTALL = "chocoinstall", "Chocolatey Software Install"
    RUN_CMD = "runcmd", "Run Command"
    RUN_SCRIPT = "runscript", "Run Script"
    RUN_PATCH_SCAN = "runpatchscan", "Run Patch Scan"
    RUN_PATCH_INSTALL = "runpatchinstall", "Run Patch Install"


class CheckType(models.TextChoices):
    DISK_SPACE = "diskspace", "Disk Space Check"
    PING = "ping", "Ping Check"
    CPU_LOAD = "cpuload", "CPU Load Check"
    MEMORY = "memory", "Memory Check"
    WINSVC = "winsvc", "Service Check"
    SCRIPT = "script", "Script Check"
    EVENT_LOG = "eventlog", "Event Log Check"


class AuditActionType(models.TextChoices):
    LOGIN = "login", "User Login"
    FAILED_LOGIN = "failed_login", "Failed User Login"
    DELETE = "delete", "Delete Object"
    MODIFY = "modify", "Modify Object"
    ADD = "add", "Add Object"
    VIEW = "view", "View Object"
    CHECK_RUN = "check_run", "Check Run"
    TASK_RUN = "task_run", "Task Run"
    AGENT_INSTALL = "agent_install", "Agent Install"
    REMOTE_SESSION = "remote_session", "Remote Session"
    EXEC_SCRIPT = "execute_script", "Execute Script"
    EXEC_COMMAND = "execute_command", "Execute Command"
    BULK_ACTION = "bulk_action", "Bulk Action"
    URL_ACTION = "url_action", "URL Action"


class AuditObjType(models.TextChoices):
    USER = "user", "User"
    SCRIPT = "script", "Script"
    AGENT = "agent", "Agent"
    POLICY = "policy", "Policy"
    WINUPDATE = "winupdatepolicy", "Patch Policy"
    CLIENT = "client", "Client"
    SITE = "site", "Site"
    CHECK = "check", "Check"
    AUTOTASK = "automatedtask", "Automated Task"
    CORE = "coresettings", "Core Settings"
    BULK = "bulk", "Bulk"
    ALERT_TEMPLATE = "alerttemplate", "Alert Template"
    ROLE = "role", "Role"
    URL_ACTION = "urlaction", "URL Action"
    KEYSTORE = "keystore", "Global Key Store"
    CUSTOM_FIELD = "customfield", "Custom Field"


class DebugLogLevel(models.TextChoices):
    INFO = "info", "Info"
    WARN = "warning", "Warning"
    ERROR = "error", "Error"
    CRITICAL = "critical", "Critical"


class DebugLogType(models.TextChoices):
    AGENT_UPDATE = "agent_update", "Agent Update"
    AGENT_ISSUES = "agent_issues", "Agent Issues"
    WIN_UPDATES = "win_updates", "Windows Updates"
    SYSTEM_ISSUES = "system_issues", "System Issues"
    SCRIPTING = "scripting", "Scripting"


# Agent db fields that are not needed for most queries, speeds up query
AGENT_DEFER = (
    "wmi_detail",
    "services",
    "created_by",
    "created_time",
    "modified_by",
    "modified_time",
)

ONLINE_AGENTS = (
    "pk",
    "agent_id",
    "last_seen",
    "overdue_time",
    "offline_time",
    "version",
)

FIELDS_TRIGGER_TASK_UPDATE_AGENT = [
    "run_time_bit_weekdays",
    "run_time_date",
    "expire_date",
    "daily_interval",
    "weekly_interval",
    "enabled",
    "remove_if_not_scheduled",
    "run_asap_after_missed",
    "monthly_days_of_month",
    "monthly_months_of_year",
    "monthly_weeks_of_month",
    "task_repetition_duration",
    "task_repetition_interval",
    "stop_task_at_duration_end",
    "random_task_delay",
    "run_asap_after_missed",
    "task_instance_policy",
]

POLICY_TASK_FIELDS_TO_COPY = [
    "alert_severity",
    "email_alert",
    "text_alert",
    "dashboard_alert",
    "name",
    "actions",
    "run_time_bit_weekdays",
    "run_time_date",
    "expire_date",
    "daily_interval",
    "weekly_interval",
    "task_type",
    "enabled",
    "remove_if_not_scheduled",
    "run_asap_after_missed",
    "custom_field",
    "collector_all_output",
    "monthly_days_of_month",
    "monthly_months_of_year",
    "monthly_weeks_of_month",
    "task_repetition_duration",
    "task_repetition_interval",
    "stop_task_at_duration_end",
    "random_task_delay",
    "run_asap_after_missed",
    "task_instance_policy",
    "continue_on_error",
]

CHECKS_NON_EDITABLE_FIELDS = [
    "check_type",
    "overridden_by_policy",
    "created_by",
    "created_time",
    "modified_by",
    "modified_time",
]

POLICY_CHECK_FIELDS_TO_COPY = [
    "warning_threshold",
    "error_threshold",
    "alert_severity",
    "name",
    "run_interval",
    "disk",
    "fails_b4_alert",
    "ip",
    "script",
    "script_args",
    "info_return_codes",
    "warning_return_codes",
    "timeout",
    "svc_name",
    "svc_display_name",
    "svc_policy_mode",
    "pass_if_start_pending",
    "pass_if_svc_not_exist",
    "restart_if_stopped",
    "log_name",
    "event_id",
    "event_id_is_wildcard",
    "event_type",
    "event_source",
    "event_message",
    "fail_when",
    "search_last_days",
    "number_of_events_b4_alert",
    "email_alert",
    "text_alert",
    "dashboard_alert",
]


WEEK_DAYS = {
    "Sunday": 0x1,
    "Monday": 0x2,
    "Tuesday": 0x4,
    "Wednesday": 0x8,
    "Thursday": 0x10,
    "Friday": 0x20,
    "Saturday": 0x40,
}

MONTHS = {
    "January": 0x1,
    "February": 0x2,
    "March": 0x4,
    "April": 0x8,
    "May": 0x10,
    "June": 0x20,
    "July": 0x40,
    "August": 0x80,
    "September": 0x100,
    "October": 0x200,
    "November": 0x400,
    "December": 0x800,
}

WEEKS = {
    "First Week": 0x1,
    "Second Week": 0x2,
    "Third Week": 0x4,
    "Fourth Week": 0x8,
    "Last Week": 0x10,
}

MONTH_DAYS = {f"{b}": 0x1 << a for a, b in enumerate(range(1, 32))}
MONTH_DAYS["Last Day"] = 0x80000000

DEMO_NOT_ALLOWED = [
    {"name": "AgentProcesses", "methods": ["DELETE"]},
    {"name": "AgentMeshCentral", "methods": ["GET", "POST"]},
    {"name": "update_agents", "methods": ["POST"]},
    {"name": "send_raw_cmd", "methods": ["POST"]},
    {"name": "install_agent", "methods": ["POST"]},
    {"name": "GenerateAgent", "methods": ["GET"]},
    {"name": "email_test", "methods": ["POST"]},
    {"name": "server_maintenance", "methods": ["POST"]},
    {"name": "CodeSign", "methods": ["PATCH", "POST"]},
    {"name": "TwilioSMSTest", "methods": ["POST"]},
    {"name": "GetEditActionService", "methods": ["PUT", "POST"]},
    {"name": "TestScript", "methods": ["POST"]},
    {"name": "GetUpdateDeleteAgent", "methods": ["DELETE"]},
    {"name": "Reboot", "methods": ["POST", "PATCH"]},
    {"name": "recover", "methods": ["POST"]},
    {"name": "run_script", "methods": ["POST"]},
    {"name": "bulk", "methods": ["POST"]},
    {"name": "WMI", "methods": ["POST"]},
    {"name": "PolicyAutoTask", "methods": ["POST"]},
    {"name": "RunAutoTask", "methods": ["POST"]},
    {"name": "run_checks", "methods": ["POST"]},
    {"name": "GetSoftware", "methods": ["POST", "PUT"]},
    {"name": "ScanWindowsUpdates", "methods": ["POST"]},
    {"name": "InstallWindowsUpdates", "methods": ["POST"]},
    {"name": "PendingActions", "methods": ["DELETE"]},
    {"name": "clear_cache", "methods": ["GET"]},
]

LINUX_NOT_IMPLEMENTED = [
    {"name": "ScanWindowsUpdates", "methods": ["POST"]},
    {"name": "GetSoftware", "methods": ["POST", "PUT"]},
    {"name": "Reboot", "methods": ["PATCH"]},  # TODO implement reboot later
]
