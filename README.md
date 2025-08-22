Clone existing repo
- `git clone https://github.com/wherethereisawill/shipfast.git new-project-name`
- `cd new-project-name`

Remove the link to the old remote
- `git remote remove origin`

Create new repo on Github
- `https://github.com/new`

Point local repo to new remote
- `git remote add origin https://github.com/wherethereisawill/<new-repo>.git`

Push everything up to new remote
- `git branch -M main`
- `git push -u origin main`

Install backend deps and run
- `cd backend`
- `uv sync`
- `uvicorn main:app --reload --host 0.0.0.0 --port 8000`

Install frontend deps & run
- `npm install`
- `npm run dev`