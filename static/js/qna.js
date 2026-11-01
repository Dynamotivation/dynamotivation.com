// Animated open/close for FAQ items (details.qna-item).
//
// The answer panel's height is animated with the Web Animations API, so opening
// and closing share one code path and can be interrupted mid-way without a jump.
// Without JavaScript, or when the visitor prefers reduced motion, the native
// <details> behaviour is left alone and the items toggle instantly.
document.addEventListener('DOMContentLoaded', function () {
    const reducedMotion = window.matchMedia('(prefers-reduced-motion: reduce)');
    const DURATION = 280;
    const EASING = 'cubic-bezier(0.2, 0.7, 0.2, 1)';

    document.querySelectorAll('details.qna-item').forEach(function (item) {
        const summary = item.querySelector('.qna-question');
        const panel = item.querySelector('.qna-answer');
        if (!summary || !panel) {
            return;
        }

        // Open the item that a link such as /page/#qna-... points at.
        if (item.id && window.location.hash === '#' + item.id) {
            item.open = true;
        }

        let animation = null;
        let wantOpen = item.open;

        summary.addEventListener('click', function (event) {
            if (reducedMotion.matches) {
                return;
            }
            event.preventDefault();
            wantOpen = !wantOpen;

            // Start from whatever height is on screen right now, so a click during
            // an animation reverses it smoothly instead of snapping.
            const from = item.open ? panel.getBoundingClientRect().height : 0;
            if (animation) {
                animation.cancel();
                animation = null;
            }

            if (wantOpen) {
                item.open = true;
                const to = panel.scrollHeight;
                animation = panel.animate(
                    { height: [from + 'px', to + 'px'], opacity: [from ? 1 : 0, 1] },
                    { duration: DURATION, easing: EASING }
                );
                animation.onfinish = function () {
                    animation = null;
                };
            } else {
                animation = panel.animate(
                    { height: [from + 'px', '0px'], opacity: [1, 0] },
                    { duration: DURATION, easing: EASING, fill: 'forwards' }
                );
                animation.onfinish = function () {
                    item.open = false;
                    animation.cancel();
                    animation = null;
                };
            }
        });
    });
});
