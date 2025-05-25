# Task_2_College
Task for college lesson.

Pipeline GitHub Actions:
- Buduje obraz aplikacji pogodowej (FastAPI),
- Wspiera architektury: `amd64` i `arm64`,
- Używa cache w DockerHub (`valdegor/cache-zad2:cache`),
- Skanuje Trivy – puszcza obraz do GHCR tylko bez CVE HIGH/CRITICAL.

## Tagowanie:
- `latest` – wersja stabilna
- Cache: `valdegor/cache-zad2:cache`

## Skaner bezpieczeństwa:
- Trivy (`aquasecurity/trivy-action`)
