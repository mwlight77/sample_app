import { Card, CardActions, CardContent, Typography } from "@mui/material"
import type { Book } from "./Types"

const BookComponent = ({ book }: { book: Book }) => {
    return (
        <Card>
            <CardContent>
                <Typography variant="h5">{book.title}</Typography>
                <Typography variant="subtitle1">{book.author}</Typography>
                <Typography variant="body2">Date Added: {book.dateAdded}</Typography>
            </CardContent>
            <CardActions>
                {/* Add any actions here */}
            </CardActions>
        </Card>
    )
}

export default BookComponent