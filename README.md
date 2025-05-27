# Task_2_College
Task for college lesson.

Pipeline GitHub Actions:
- Buduje obraz aplikacji pogodowej (FastAPI),
- Wspiera architektury: `amd64` i `arm64`,
- Używa cache w DockerHub (`valdegor/cache-zad2:cache`),
- Skanuje z Docker Hubem – puszcza obraz do GHCR tylko bez CVE HIGH/CRITICAL.

## Tagowanie:
- `latest` – wersja stabilna
- Repo: `matthewl72483/labs`
- Obraz: `latest`

## Skaner bezpieczeństwa:
- Github Scout
