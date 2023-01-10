# hra-osu-pygame

## Jaké objekty budou v hře vykresleny?

Ve hře bude počítadlo skóre a míčky na bílém pozadí.

## Jaké budou mít objekty vlastnosti (např. barva, velikost, pozice)?

Na bílém pozadí se budou generovat modré míčky, které se v každé další ze tří úrovní menší a menší. Počitadlo skóre bude ve formě černého textu umístěno vlevo nahoře.

## Jaké akce budou hráči moci v hře provádět (např. pohyb, skórování, změna úrovně)?

Hráč se bude snažit v omezeném časovém limitu přesunout myš na modrý míček a stisknout mezerník, čímž získá bod.

## Co se stane, když hráč dosáhne určitého skóre nebo úrovně?

Jakmile hráč dosáhne 10 bodů, postoupí do další úrovně. Po třetí úrovni se hra zastaví a zobrazí se **game over**.

## Jak budou objekty v hře interagovat (např. kolize, sbírání předmětů)?

V základní verzi hry se míčky nebudou pohybovat, to bude až další úkol po zprovoznění základního mechanismu.

## Jak budou hranice hry a jiné překážky definovány? (např. "Pokud se objekt dostane mimo hranice hry, vrátí se na začátek.")

V základní verzi hry hranice nejsou.

## Jak budou hráči v hře ovlivňovat okolí nebo interagovat s ostatními objekty? (např. "Pokud hráč narazí do překážky, skóre se sníží o jednu jednotku.")

V základní verzi hry hranice nejsou.

## Jak budou v hře generovány nové objekty nebo překážky?

Každých 3-7 sekund se vytvoří nový míček na na náhodné pozici na obrazovce. Míčky, které se generují bezprostředně po sobě se nesmí zobrazit na sobě.

## Jak budou v hře zobrazovány skóre nebo úrovně? (např. "Skóre se zobrazí v pravém horním rohu obrazovky a aktualizuje se po každém úspěšném překonání překážky.")

Skóre se zobrazuje v levém horním rohu ve formátu Skóre: *číslo*. Úrovně se uživateli zobrazovat nebudou.