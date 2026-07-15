def get_banner(hero_base64: str) -> str:
    """
    Return the home page banner HTML.

    Parameters
    ----------
    hero_base64 : str
        Base64 encoded hero image.

    Returns
    -------
    str
        Banner HTML.
    """

    banner = """
<style>
  .hero-banner {
    width: 100%;
    max-width: 1100px;
    height: auto;
    min-height: 240px;
    margin: 0 auto 24px auto;
    display: flex;
    align-items: center;
    gap: 30px;
    padding: 25px 45px;
    border-radius: 22px;
    position: relative;
    overflow: hidden;
    background: linear-gradient(90deg,#182a96 0%,#3729b6 40%,#6c31d7 75%,#a33cff 100%);
    box-shadow: 0 10px 25px rgb(28 25 25 / 44%);
  }

  .hero-image img {
    width: 220px;
    object-fit: contain;
  }

  .hero-content h3 {
    margin: 0 0 6px 0;
    font-size: 40px;
    font-weight: 800;
    letter-spacing: 1px;
    color: #ffffff;
  }

  .hero-content h1 {
    margin: 2px 0 6px 0;
    font-size: 50px;
    font-weight: 800;
    line-height: 1.15;
    color: #ffffff;
  }

  .hero-content p {
    margin: 2px 0 0 0;
    font-size: 18px;
    font-weight: 500;
    color: #ffffff;
    word-spacing: 25px;
  }

  .white-text { color: #ffffff; }
  .blue-text { color: #4FC3FF; }

.hero-banner::before {
    content: "";
    position: absolute;
    width: 160%;
    height: 240px;
    top: 40px;
    left: 20%;
    background: radial-gradient(circle at center,
        rgba(255, 255, 255, .16) 1px,
        transparent 1px);
    background-size: 14px 14px;
    opacity: .15;
}
.hero-banner::after {
    content: "";
    position: absolute;
    width: 140%;
    height: 200px;
    top: -40px;
    left: 30%;
    background: repeating-radial-gradient(circle at center,
        rgba(255, 255, 255, .15) 0px,
        rgba(255, 255, 255, .15) 2px,
        transparent 3px,
        transparent 18px);
    opacity: .10;
    transform: rotate(-8deg);
}
.dots {
    position: absolute;
    right: 60px;
    top: 45px;
    width: 80px;
    height: 80px;
    background-image: radial-gradient(rgba(255, 255, 255, .45) 2px,
        transparent 5px);
    background-size: 14px 14px;
    opacity: .7;
}
</style>

<div class="hero-banner">
  <div class="hero-image">
    <img src="HERO_IMG_PLACEHOLDER" alt="Dashboard Illustration">
  </div>
  <div class="hero-content">
    <h3 class="white-text">Generic Automated</h3>
    <h1>
      <span class="white-text">Data</span>
      <span class="blue-text">Analytics</span>
      <span class="white-text">Dashboard</span>
    </h1>
    <p class="white-text">
      | Upload     | Analyze     | Visualize     | Report |
    </p>
  </div>
</div>
"""

    return banner.replace(
        "HERO_IMG_PLACEHOLDER",
        f"data:image/png;base64,{hero_base64}"
    )