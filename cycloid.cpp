#include <SFML/Graphics.hpp>
#include <cmath>
#include <vector>

// 상수 정의
const float PI = 3.14159265358979323846f;

// 사이클로이드 생성 함수
std::vector<sf::Vertex> generateCycloid(float r, float t_max, float dt, sf::Vector2f offset) {
    std::vector<sf::Vertex> points;
    for (float t = 0; t <= t_max; t += dt) {
        float x = r * (t - sin(t));
        float y = r * (1 - cos(t));
        points.push_back(sf::Vertex(sf::Vector2f(x, y) + offset, sf::Color::Red));
    }
    return points;
}

// 에피사이클로이드 생성 함수 (큰 원의 바깥에서 굴러가는 경우)
std::vector<sf::Vertex> generateEpicycloid(float R, float r, float t_max, float dt, sf::Vector2f offset) {
    std::vector<sf::Vertex> points;
    for (float t = 0; t <= t_max; t += dt) {
        float factor = (R + r) / r;
        float x = (R + r) * cos(t) - r * cos(factor * t);
        float y = (R + r) * sin(t) - r * sin(factor * t);
        points.push_back(sf::Vertex(sf::Vector2f(x, y) + offset, sf::Color::Green));
    }
    return points;
}

// 하이포사이클로이드 생성 함수 (큰 원의 안쪽에서 굴러가는 경우)
std::vector<sf::Vertex> generateHypocycloid(float R, float r, float t_max, float dt, sf::Vector2f offset) {
    std::vector<sf::Vertex> points;
    for (float t = 0; t <= t_max; t += dt) {
        float factor = (R - r) / r;
        float x = (R - r) * cos(t) + r * cos(factor * t);
        float y = (R - r) * sin(t) - r * sin(factor * t);
        points.push_back(sf::Vertex(sf::Vector2f(x, y) + offset, sf::Color::Blue));
    }
    return points;
}

int main() {
    // SFML 창 생성 (800x600)
    sf::RenderWindow window(sf::VideoMode(800, 600), "Cycloid, Epicycloid, Hypocycloid Visualization");
    window.setFramerateLimit(60);

    // 곡선 표시를 위한 오프셋 설정 (창 내에 좌우로 3개의 영역 분할)
    sf::Vector2f offsetCycloid(50, 300);      // 좌측 영역
    sf::Vector2f offsetEpicycloid(300, 300);    // 중간 영역
    sf::Vector2f offsetHypocycloid(550, 300);   // 우측 영역

    // 매개변수 설정 및 t 범위, dt 설정
    float t_max = 10 * PI;  // 충분한 주기 수
    float dt = 0.01f;

    // 각 곡선의 파라미터 설정
    float rCycloid = 30.0f; // 사이클로이드의 원 반지름
    float R_epi = 70.0f, r_epi = 20.0f;      // 에피사이클로이드 (큰 원 반지름 R, 작은 원 반지름 r)
    float R_hypo = 70.0f, r_hypo = 20.0f;      // 하이포사이클로이드 (큰 원 R, 작은 원 r)

    // 각 곡선의 점 목록 생성
    auto cycloidPoints = generateCycloid(rCycloid, t_max, dt, offsetCycloid);
    auto epicycloidPoints = generateEpicycloid(R_epi, r_epi, t_max, dt, offsetEpicycloid);
    auto hypocycloidPoints = generateHypocycloid(R_hypo, r_hypo, t_max, dt, offsetHypocycloid);

    // 메인 루프 (창이 열려있는 동안 반복)
    while (window.isOpen()) {
        sf::Event event;
        while (window.pollEvent(event)) {
            if (event.type == sf::Event::Closed)
                window.close();
        }

        // 창 초기화 (배경 흰색)
        window.clear(sf::Color::White);

        // 사이클로이드 그리기 (sf::LineStrip 사용)
        if (!cycloidPoints.empty()) {
            sf::VertexArray cycloid(sf::LineStrip, cycloidPoints.size());
            for (size_t i = 0; i < cycloidPoints.size(); i++)
                cycloid[i] = cycloidPoints[i];
            window.draw(cycloid);
        }

        // 에피사이클로이드 그리기
        if (!epicycloidPoints.empty()) {
            sf::VertexArray epi(sf::LineStrip, epicycloidPoints.size());
            for (size_t i = 0; i < epicycloidPoints.size(); i++)
                epi[i] = epicycloidPoints[i];
            window.draw(epi);
        }

        // 하이포사이클로이드 그리기
        if (!hypocycloidPoints.empty()) {
            sf::VertexArray hypo(sf::LineStrip, hypocycloidPoints.size());
            for (size_t i = 0; i < hypocycloidPoints.size(); i++)
                hypo[i] = hypocycloidPoints[i];
            window.draw(hypo);
        }

        // 창 갱신
        window.display();
    }
    return 0;
}
