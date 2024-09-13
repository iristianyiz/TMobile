from tmode_qod import TmodeQod, Environment

sdk = TmodeQod(
    client_id="tmon-i98Bo7GwLDnAtyROcw44kNQA4vEUoVMA",
    client_secret="po3169iWK5RGmM2IS",
    private_key="-----BEGIN PRIVATE KEY-----privatekey",
    base_url=Environment.DEFAULT.value,
    timeout=10000,
)

result = sdk.session.get_session(
    session_id="123e4567-e89b-12d3-a456-426614174000",
    x_correlator="233b55ed-4a48-4f33-9efe-6fc277f66e8d",
)

print(result)
