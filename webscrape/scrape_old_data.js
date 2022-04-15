$$(".profile").map((profile) => {
  var [a, p, div] = profile.children;
  let name = a.children[1].textContent;
  let image = a.children[0].children[0].style.backgroundImage;
  let split = a.href.split("/");
  let code = split[split.length - 2];
  let desc = p.textContent.trim();
  // some profiles from 2014 have a Founding Member element we need to
  // conditionally skip to scrape the right data
  if (profile.children.length == 4) {
    div = profile.children[3];
  }
  let socials = {
    github: "",
    linkedin: "",
    twitter: "",
    email: "",
    facebook: "",
  };
  for (var i = 0; i < div.children.length; i++) {
    let a = div.children[i];
    let address = a.href;
    var platform = a.children[0].classList[1].split("-")[1];
    if (platform === "envelope") {
      platform = "email";
    }
    if (
      !["github", "linkedin", "twitter", "email", "facebook"].includes(platform)
    ) {
      continue;
    }
    socials[platform] = address;
  }
  return {
    name: name,
    image: image,
    code: code,
    desc: desc,
    socials: socials,
  };
});
