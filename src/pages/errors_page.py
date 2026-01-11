from pages.base_page import BasePage


class ErrorsPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.network_fail = self.test_id("network-fail")
        self.timeout_1s = self.test_id("timeout-1s")
        self.timeout_5s = self.test_id("timeout-5s")
        self.timeout_30s = self.test_id("timeout-30s")
        self.partial_good = self.test_id("partial-good")
        self.partial_fail = self.test_id("partial-fail")
        self.leak_start = self.test_id("leak-start")
        self.audit_log = self.test_id("audit-log")

        self.security_injection = self.test_id("security-injection")
        self.security_access = self.test_id("security-access")
        self.security_xss = self.test_id("security-xss")
        self.security_vuln = self.test_id("security-vuln")
        self.security_ssrf = self.test_id("security-ssrf")
        self.security_crypto = self.test_id("security-crypto")
        self.security_logging = self.test_id("security-logging")

    def trigger_network_fail(self) -> None:
        self.click(self.network_fail)

    def trigger_timeouts(self) -> None:
        self.click(self.timeout_1s)
        self.click(self.timeout_5s)
        self.click(self.timeout_30s)

    def partial_good_visible(self) -> bool:
        return self.get(self.partial_good).is_displayed()

    def partial_fail_visible(self) -> bool:
        return self.get(self.partial_fail).is_displayed()

    def start_leak(self) -> None:
        self.click(self.leak_start)

    def audit_log_text(self) -> str:
        return self.get(self.audit_log).text

    def run_security_labs(self) -> None:
        self.click(self.security_injection)
        self.click(self.security_access)
        self.click(self.security_xss)
        self.click(self.security_vuln)
        self.click(self.security_ssrf)
        self.click(self.security_crypto)
        self.click(self.security_logging)
