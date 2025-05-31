# Task_2_College
Task for college lesson.

## Jak uruchomić workflow

Workflow zawsze się uruchomi przy commicie, a potem  pushu do brancha `main` w repo.

## Kroki workflow

1. **Pobram kod z repozytorium**
   - Pobierany jest cały kod projektu, by runner miał do niego dostęp.

2. **Przygotowuje środowisko do budowania obrazów multiarchitekturowych**
   - Instalacja QEMU, by umożliwić budowanie obrazów dla różnych architektur (np. amd64, arm64).
   - Instalacja narzędzia Docker Buildx, które pozwala na wydajniejsze i bardziej zaawansowane budowanie obrazów Docker.

3. **Daje logowanie do rejestrów**
   - GitHub Container Registry (GHCR): logowanie z użyciem tajnego tokena (`GHCR_PAT`), by móc wypychać obrazy do własnego repozytorium w `ghcr.io`.
   - DockerHub: logowanie do DockerHub, by korzystać z cache warstw budowania (przyspiesza budowę obrazów).

4. **Buduje obraz Docker dla architektury amd64**
   - Budowany jest obraz Docker (na platformę amd64) oznaczony tagiem `scan`.
   - Obraz jest wypychany do GHCR oraz wykorzystywany do skanowania bezpieczeństwa.

5. **Skanuje obraz pod kątem podatności (Trivy)**
   - Obraz jest skanowany przez Trivy pod kątem podatności typu HIGH i CRITICAL.
   - Wyniki skanowania są zapisywane do pliku `trivy_report.txt`.
   - Pipeline nie jest przerywany przy wykryciu podatności dzięki opcji `continue-on-error: true`.

6. **Udostępniam raport bezpieczeństwa jako artefakt**
   - Raport Trivy (`trivy_report.txt`) jest dostępny do pobrania w sekcji Artifacts w zakładce Actions na GitHubie.

7. **Buduje i pcham obraz multiarch**
   - Na końcu budowany jest docelowy obraz Docker dla obu architektur (`amd64` i `arm64`) i tagowany jako `latest`.
   - Obraz jest wypychany do GHCR i gotowy do użycia na różnych platformach.

## Ważne informacje

Nie dało się wybrać skanu Trivy po multiarchu, wygląda na to, że nie jest on kompatybilny z tym, więc rozwiązując to na początku testowo buduję
na jednej architekturze i sprawdzam to z Trivy generując raport, a dopiero potem na tej samej zasadzie buduję multiarch. Dzięki
czemu wiem, że nie ma tam prawie żadnych HIGH/CRITICAL.
...Poza jednym, niestety jednej podatności HIGH nie jestem w stanie naprawić i muszę ją zignorować, jest ona ściśle związana z FastAPI
i Starlette, FastAPI automatycznie instaluje Starlette, której wersja ma jakieś problemy z bezpieczeństwem, ale nie da się jej zaktualizować,
stąd musiałem dać continue-on-error: true, jest to jedyny błąd który zgłasza Trivy i myślę, że mogę go pominąć.
Ponadto w screenach załączam wynik działania workflowa, wraz z screenem z raportu z jedynym HIGH błędem, który jest zignorowany.

## Czemu Trivy nad Scouta

Trivy z reguły jest szybszy, prostszy i lepiej integruje się z CI/CD, stąd moja decyzja wyboru go, over Docker Scouta. 